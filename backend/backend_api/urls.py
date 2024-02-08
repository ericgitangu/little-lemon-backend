from .views import UserRegistrationView, CurrentUserView, UserTokenView, MenuItemListView, MenuItemDetailView, MenuItemCreateView, MenuItemUpdateView, MenuItemDeleteView, ManagerUserListView, ManagerUserCreateView, ManagerUserDeleteView, DeliveryCrewUserListView, DeliveryCrewUserCreateView, DeliveryCrewUserDeleteView, AssignOrderView, CartItemListView, OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView, CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, ChangeOrderStatusView, ChangeFeaturedItemView
from django.urls import path

from .views import *

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
    path('token/login', UserTokenView.as_view(), name='user-login'),
    path('token/logout', UserTokenView.as_view(), name='user-logout'),
    path('menu-items/', MenuItemListView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('menu-items/create/', MenuItemCreateView.as_view(), name='menu-item-create'),
    path('menu-items/update/<int:pk>/', MenuItemUpdateView.as_view(), name='menu-item-update'),
    path('menu-items/delete/<int:pk>/', MenuItemDeleteView.as_view(), name='menu-item-delete'),
    path('manager-users/', ManagerUserListView.as_view(), name='manager-user-list'),
    path('manager-users/create/', ManagerUserCreateView.as_view(), name='manager-user-create'),
    path('manager-assign-order/<int:pk>/', AssignOrderView.as_view(), name='assign-order'),
    path('manager-users/delete/<int:pk>/', ManagerUserDeleteView.as_view(), name='manager-user-delete'),
    path('manager-featured-item/<int:pk>/', ChangeFeaturedItemView.as_view(), name='change-featured-item'),
    path('delivery-crew-users/', DeliveryCrewUserListView.as_view(), name='delivery-crew-user-list'),
    path('delivery-crew-users/create/', DeliveryCrewUserCreateView.as_view(), name='delivery-crew-user-create'),
    path('delivery-crew-users/delete/<int:pk>/', DeliveryCrewUserDeleteView.as_view(), name='delivery-crew-user-delete'),
    path('delivery-crew/change-status/<int:pk>/',
         ChangeOrderStatusView.as_view(), name='change-order-status'),
    path('cart/', CartItemListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartItemListView.as_view(), name='cart-detail'),
    path('cart/create/', CartItemCreateView.as_view(), name='cart-create'),
    path('cart/update/<int:pk>/', CartItemUpdateView.as_view(), name='cart-update'),
    path('cart/delete/<int:pk>/', CartItemDeleteView.as_view(), name='cart-delete'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),    
    
]


