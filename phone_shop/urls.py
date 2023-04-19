from django.urls import path
from . import views


urlpatterns = [
    path("", views.PhoneListView.as_view(), name="phone_list"),
    path("phone_list/<int:id>/", views.PhoneDetailView.as_view(), name="phone_detail"),
    path("phone_list/<int:id>/delete/", views.PhoneDeleteView.as_view(), name="delete"),
    path("phone_list/<int:id>/update/", views.PhoneUpdateView.as_view(), name="update"),
    path("create_phone/", views.CreatePhoneView.as_view(), name="create"),
    path("search/", views.Search.as_view(), name="search"),
]
