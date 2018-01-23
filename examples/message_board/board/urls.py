from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'clear_all', views.clear_all, name='clear_all'),
]