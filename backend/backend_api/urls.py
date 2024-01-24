from .views import UserRegistrationView, CurrentUserView, UserTokenView, MenuItemListView, MenuItemDetailView, MenuItemCreateView, MenuItemUpdateView, MenuItemDeleteView, ManagerUserListView, ManagerUserCreateView, ManagerUserDeleteView, DeliveryCrewUserListView, DeliveryCrewUserCreateView, DeliveryCrewUserDeleteView
from django.urls import path

from .views import (
    UserRegistrationView,
    CurrentUserView,
    UserTokenView,
    MenuItemListView,
    MenuItemDetailView,
    MenuItemCreateView,
    MenuItemUpdateView,
    MenuItemDeleteView,
    ManagerUserListView,
    ManagerUserCreateView,
    ManagerUserDeleteView,
    DeliveryCrewUserListView,
    DeliveryCrewUserCreateView,
    DeliveryCrewUserDeleteView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
    path('token/', UserTokenView.as_view(), name='user-token'),
    path('menu-items/', MenuItemListView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('menu-items/create/', MenuItemCreateView.as_view(), name='menu-item-create'),
    path('menu-items/update/<int:pk>/', MenuItemUpdateView.as_view(), name='menu-item-update'),
    path('menu-items/delete/<int:pk>/', MenuItemDeleteView.as_view(), name='menu-item-delete'),
    path('manager-users/', ManagerUserListView.as_view(), name='manager-user-list'),
    path('manager-users/create/', ManagerUserCreateView.as_view(), name='manager-user-create'),
    path('manager-users/delete/<int:pk>/', ManagerUserDeleteView.as_view(), name='manager-user-delete'),
    path('delivery-crew-users/', DeliveryCrewUserListView.as_view(), name='delivery-crew-user-list'),
    path('delivery-crew-users/create/', DeliveryCrewUserCreateView.as_view(), name='delivery-crew-user-create'),
    path('delivery-crew-users/delete/<int:pk>/', DeliveryCrewUserDeleteView.as_view(), name='delivery-crew-user-delete'),
]


