# pylint: disable=invalid-name
from rest_framework.authtoken import views
from django.conf.urls import url
from django.urls import include

app_name = 'users'
urlpatterns = [
    url(r'^ajudaai/', include('djoser.urls')),
    url(r'^ajudaai/', include('djoser.urls.authtoken')),
]
