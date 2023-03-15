from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_world_view, name='hello'),
    path('posts/', views.post_view, name='posts'),
]