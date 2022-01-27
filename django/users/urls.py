# pylint: disable=invalid-name
from django.conf.urls import url
from django.urls import include

app_name = 'users'
urlpatterns = [
    url('', include('djoser.urls')),
    url('', include('djoser.urls.authtoken')),
]
