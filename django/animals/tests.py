from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from animals.models import Animal


class AnimalTests(APITestCase):
    """
    Tests for Animal endpoints.
    """

    def setUp(self):
        Animal.objects.create(name='Dummy Animal 1', description='Dummy Description')
        Animal.objects.create(name='Dummy Animal 2', description='Dummy Description')
        Animal.objects.create(name='Dummy Animal 3', description='Dummy Description', allow_send_invite_repository=False)

    def test_animal_list(self):
        """
        Ensure we can list the animal objects.
        """
        url = reverse('animal-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Animal.objects.count(), 3)

    def test_animal_list_filtered(self):
        """
        Ensure we can list the animal objects filtered by allow invite boolean.
        """
        url = f'{reverse("animal-list")}?allow-send-invite-repository=true'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_animal_create(self):
        """
        Ensure we can create a new animal object.
        """
        url = reverse('animal-list')
        data = {'name': 'Dummy Create Animal', 'description': 'Dummy Create Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Animal.objects.count(), 4)
        self.assertEqual(Animal.objects.get(name='Dummy Create Animal').description, 'Dummy Create Description')

    def test_animal_put(self):
        """
        Ensure we can edit a animal object.
        """
        dummy_animal = Animal.objects.get(name='Dummy Animal 1')
        data = {'name': 'Dummy Animal 1', 'description': 'Dummy Description Edited'}
        url = f'{reverse("animal-list")}{dummy_animal.id}/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Animal.objects.get(name='Dummy Animal 1').description, 'Dummy Description Edited')

    def test_animal_delete(self):
        """
        Ensure we can delete a animal object.
        """
        dummy_animal = Animal.objects.create(name='Dummy Deletion Animal', description='Dummy Description')
        url = f'{reverse("animal-list")}{dummy_animal.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Animal.objects.filter(enabled=False).count(), 1)

    def test_deleted_animal_list(self):
        """
        Ensure we can list the deleted animal objects.
        """
        Animal.objects.create(name='Dummy Animal', description='Dummy Description', enabled=False)
        url = f'{reverse("animal-list")}deleted/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
