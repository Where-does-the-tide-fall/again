from django.urls import re_path
from start_again import views

urlpatterns = [
    re_path('^first/$', views.register),
    re_path('^login/$', views.login)
]
