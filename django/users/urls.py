from django.urls import re_path
from rest_framework.authtoken import views


app_name = 'users'
urlpatterns = [
    re_path(r'^token-auth/', views.obtain_auth_token)
]
