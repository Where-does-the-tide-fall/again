from django.urls import re_path
from HelloPython import views
urlpatterns = [
    re_path(r'^hello/$', views.hello_views)
]