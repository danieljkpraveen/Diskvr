from django.urls import path

from . import views


app_name = "inventory"

urlpatterns = [
    path("", views.items, name="items"),
    path("<uuid:pk>", views.detail, name="detail"),
    path("new/", views.new, name="new"),
    path("<uuid:pk>/delete/", views.delete, name="delete"),
    path("<uuid:pk>/edit/", views.edit, name="edit"),
    path("orders/", views.orders, name="orders"),
]
