from django.urls import path
from .views import create_user, rectangle_view,index
from . import views

urlpatterns = [
    path('create-user/', create_user, name='create_user'),
    path('rectangle/', rectangle_view, name='rectangle_view'),
    path('', index, name='index'),
]
