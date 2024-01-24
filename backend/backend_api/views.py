from django.shortcuts import render
from rest_framework import generics, permissions,filters
from rest_framework.exceptions import PermissionDenied
from .serializers import *
from django.shortcuts import get_object_or_404
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

# User registration and token generation endpoints
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserTokenView(generics.CreateAPIView):
    serializer_class = UserTokenSerializer

# Menu-items endpoints
class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]

class MenuItemDetailView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]

class MenuItemCreateView(generics.CreateAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]

class MenuItemUpdateView(generics.UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]

class MenuItemDeleteView(generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]

# User group management endpoints
class ManagerUserListView(generics.ListAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class ManagerUserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class ManagerUserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class DeliveryCrewUserListView(generics.ListAPIView):
    queryset = User.objects.filter(groups__name='Delivery crew')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class DeliveryCrewUserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class DeliveryCrewUserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.filter(groups__name='Delivery crew')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

# Cart management endpoints
class CartItemListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).cart_items.all()

class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemDeleteView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).cart_items.all()

# Order management endpoints
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart_items = Cart.objects.filter(user=self.request.user).cart_items.all()
        serializer.save(user=self.request.user, order_items=cart_items)
        cart_items.delete()

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        order = super().get_object()
        if order.user != self.request.user:
            raise PermissionDenied()
        return order

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = [permissions.IsAdminUser]

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]

# Apply filtering, pagination, and sorting
class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

# API Throttling
class ThrottledView(generics.RetrieveAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    ...



# Create your views here.
