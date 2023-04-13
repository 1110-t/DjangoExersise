from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogs,name='blogs'),
    path('<int:pk>', views.blog, name='blog'),
    path('new',views.new,name='new'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('users', views.users, name='users'),
    path('user/<int:pk>', views.user, name='user'),
    path('delete/<int:pk>',views.delete,name="delete")
]