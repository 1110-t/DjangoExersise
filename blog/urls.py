from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users, name='index'),
    path('user/<int:pk>', views.user, name='user'),
]