from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from reports.models import Report


class ReportTests(APITestCase):
    """
    Tests for Report endpoints.
    """

    def setUp(self):
        Report.objects.create(name='Dummy Report 1', description='Dummy Description')
        Report.objects.create(name='Dummy Report 2', description='Dummy Description')
        Report.objects.create(name='Dummy Report 3', description='Dummy Description', allow_send_invite_repository=False)

    def test_report_list(self):
        """
        Ensure we can list the report objects.
        """
        url = reverse('report-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Report.objects.count(), 3)

    def test_report_list_filtered(self):
        """
        Ensure we can list the report objects filtered by allow invite boolean.
        """
        url = f'{reverse("report-list")}?allow-send-invite-repository=true'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_report_create(self):
        """
        Ensure we can create a new report object.
        """
        url = reverse('report-list')
        data = {'name': 'Dummy Create Report', 'description': 'Dummy Create Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Report.objects.count(), 4)
        self.assertEqual(Report.objects.get(name='Dummy Create Report').description, 'Dummy Create Description')

    def test_report_put(self):
        """
        Ensure we can edit a report object.
        """
        dummy_report = Report.objects.get(name='Dummy Report 1')
        data = {'name': 'Dummy Report 1', 'description': 'Dummy Description Edited'}
        url = f'{reverse("report-list")}{dummy_report.id}/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Report.objects.get(name='Dummy Report 1').description, 'Dummy Description Edited')

    def test_report_delete(self):
        """
        Ensure we can delete a report object.
        """
        dummy_report = Report.objects.create(name='Dummy Deletion Report', description='Dummy Description')
        url = f'{reverse("report-list")}{dummy_report.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Report.objects.filter(enabled=False).count(), 1)

    def test_deleted_report_list(self):
        """
        Ensure we can list the deleted report objects.
        """
        Report.objects.create(name='Dummy Report', description='Dummy Description', enabled=False)
        url = f'{reverse("report-list")}deleted/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
