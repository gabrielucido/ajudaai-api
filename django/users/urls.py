# pylint: disable=invalid-name
from rest_framework.authtoken import views
from django.urls import re_path

app_name = 'users'
urlpatterns = [
    re_path(r'^token-auth/', views.obtain_auth_token)
]
