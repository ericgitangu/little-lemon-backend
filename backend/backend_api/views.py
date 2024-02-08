from django.shortcuts import render
from requests import Response
from rest_framework import generics, permissions,filters, status
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Category, MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import User
# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle # implemented in the settings.py file
from .permissions import IsManager, IsOwnerOrReadOnly, IsDeliveryCrew
from .serializers import *
from rest_framework.pagination import PageNumberPagination

# User registration and token generation endpoints
class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    This view allows users to register by creating a new user object.
    It requires authentication or read-only permission and checks if the user is the owner of the object.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for User objects.
        permission_classes (list): The list of permission classes for the view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# User list and creation endpoints
class UserListView(generics.ListAPIView):
    """
    A view for listing and creating User objects.

    Inherits from `generics.ListAPIView` and provides the following functionality:
    - Lists all User objects
    - Creates a new User object

    Requires the user to be an admin.

    Methods:
    - get_queryset: Returns the queryset of User objects
    - dispatch: Handles the HTTP request and calls the appropriate method
    - get: Handles the GET request and calls the list method
    - post: Handles the POST request and calls the create method
    - perform_create: Performs additional actions after creating a User object
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return super().get_queryset()
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# User management endpoints
class UserCreateView(generics.CreateAPIView):
    """
    A view for creating a new user.

    This view allows an admin user to create a new user by sending a POST request with the required data.
    The user will be created using the UserSerializer and the current authenticated user will be set as the creator.
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return super().get_queryset()

class UserDetailView(generics.RetrieveAPIView):
    """
    A view for retrieving details of a user.

    This view retrieves the details of a user based on the provided user ID.
    Only authenticated users are allowed to access this view.

    Attributes:
        queryset (QuerySet): The queryset used to retrieve the user.
        serializer_class (Serializer): The serializer class used to serialize the user data.
        permission_classes (list): The list of permission classes applied to this view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserUpdateView(generics.UpdateAPIView):
    """
    A view for updating a user instance.

    This view allows an admin user to update the details of a user instance.
    Only admin users are allowed to access this view.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for User objects.
        permission_classes (list): The list of permission classes for this view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserDeleteView(generics.DestroyAPIView):
    """
    A view for deleting a user.

    Inherits from `generics.DestroyAPIView` and provides the functionality to delete a user.
    Requires the user to be an admin.

    Attributes:
        queryset (QuerySet): The queryset of all users.
        serializer_class (Serializer): The serializer class for the user model.
        permission_classes (list): The list of permission classes required for this view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CurrentUserView(generics.RetrieveAPIView):
    """
    A view that retrieves the currently authenticated user.

    This view returns the serialized representation of the currently authenticated user.
    Only authenticated users are allowed to access this view.

    Attributes:
        serializer_class (class): The serializer class used to serialize the user object.
        permission_classes (list): The list of permission classes that control access to this view.
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class DeleteUserView(generics.DestroyAPIView):
    """
    A view for deleting a user.

    This view allows an admin user to delete a user from the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

# User token management endpoints
class UserTokenView(generics.CreateAPIView):
    """
    View for creating and retrieving user tokens.
    """
    queryset = User.objects.all()
    serializer_class = UserTokenSerializer

    def get_queryset(self):
        return super().get_queryset()
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Menu-items endpoints
class MenuItemListView(generics.ListAPIView):
    """
    API view for retrieving a list of menu items.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']
    ordering = ['price']
    search_fields = ['category__name']  # Add this line to search by category name
    paginate_by = 5

class MenuItemDetailView(generics.RetrieveAPIView):
    """
    A view for retrieving a single menu item.

    This view allows any user to retrieve details of a specific menu item.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']
    ordering = ['price']
    # Add this line to search by category name
    search_fields = ['category__name']
    paginate_by = 5

class MenuItemCreateView(generics.CreateAPIView):
    """
    View for creating a new menu item.
    """
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]

class MenuItemUpdateView(generics.UpdateAPIView):
    """
    API view for updating a menu item.

    This view allows an admin user to update the details of a menu item.
    The `queryset` attribute specifies the set of menu items to be updated.
    The `serializer_class` attribute specifies the serializer to be used for updating the menu item.
    The `permission_classes` attribute restricts access to admin users only.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]

class MenuItemDeleteView(generics.DestroyAPIView):
    """
    API view for deleting a menu item.

    Inherits from `generics.DestroyAPIView` and provides the following features:
    - Deletes a menu item from the database.
    - Uses the `MenuItemSerializer` for serialization.
    - Requires the user to be an admin.

    Usage:
    - Send a DELETE request to the view's endpoint to delete a menu item.

    Example:
    DELETE /api/menu-items/42/

    Response:
    HTTP 204 No Content
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]

# User group management endpoints
class ManagerUserListView(generics.ListAPIView):
    """
    API view for retrieving a list of manager users.

    This view returns a list of users who belong to the 'Manager' group.

    Attributes:
        queryset (QuerySet): The queryset used to retrieve the manager users.
        serializer_class (Serializer): The serializer class used to serialize the manager users.
        permission_classes (list): The list of permission classes required to access this view.
    """
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class ManagerUserCreateView(generics.CreateAPIView):
    """
    A view for creating manager users.

    This view allows an admin user to create a new manager user by providing the necessary data.
    Only admin users are allowed to access this view.

    Serializer Class:
        UserSerializer: The serializer class used for validating and deserializing the user data.

    Permission Classes:
        IsAdminUser: Only admin users are allowed to access this view.
    """
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAdminUser]

class ManagerUserDeleteView(generics.DestroyAPIView):
    """
    A view for deleting manager users.

    This view allows an admin user to delete manager users from the system.

    Attributes:
        queryset (QuerySet): The queryset used to retrieve the manager users.
        serializer_class (Serializer): The serializer class used for serializing the manager users.
        permission_classes (list): The list of permission classes required to access this view.
    """
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

# Delivery Crew management endpoints
class DeliveryCrewUserListView(generics.ListAPIView):
    """
    API view for retrieving a list of delivery crew users.
    Only accessible to admin users.
    """
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class DeliveryCrewUserCreateView(generics.CreateAPIView):
    """
    View for creating a new delivery crew user.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, IsManager]

class DeliveryCrewUserDeleteView(generics.DestroyAPIView):
    """
    A view for deleting a delivery crew user.

    This view allows an admin user to delete a user who belongs to the 'Delivery Crew' group.
    Only admin users have permission to access this view.
    """

    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return super().get_queryset()
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Cart management endpoints
class CartItemListView(generics.ListAPIView):
    """
    API view for retrieving a list of cart items for the authenticated user.
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartItemCreateView(generics.CreateAPIView):
    """
    View for creating a new cart item.

    This view allows authenticated users to create a new cart item.
    The user's cart is automatically associated with the created cart item.
    By default, the price is set to the unit price of the menu item multiplied by the quantity.

    Attributes:
        serializer_class (Serializer): The serializer class used for validating and deserializing the request data.
        permission_classes (list): The list of permission classes that the user must satisfy to access this view.
    """

    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartItemDeleteView(generics.DestroyAPIView):
    """
    A view for deleting a cart item.

    This view allows authenticated users to delete a specific cart item from their cart.
    """

    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, user=request.user)
        menu_item = get_object_or_404(MenuItem, pk=kwargs['pk'])
        cart_item = cart.cart_items.filter(menu_item=menu_item)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()

class CartItemUpdateView(generics.UpdateAPIView):
    """
    A view for updating a cart item.

    This view allows authenticated users to update the quantity of a specific cart item in their cart.
    """

    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def put(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, user=request.user)
        menu_item = get_object_or_404(MenuItem, pk=kwargs['pk'])
        cart_item = cart.cart_items.filter(menu_item=menu_item)
        serializer = self.get_serializer(cart_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Order management endpoints
class OrderCreateView(generics.CreateAPIView):
    """
    View for creating an order.

    This view allows authenticated users to create an order by providing the necessary data.
    The order is created using the `OrderCreateSerializer` serializer and the user's cart items.
    After the order is created, the user's cart items are deleted.

    Attributes:
        serializer_class (Serializer): The serializer class to use for creating the order.
        permission_classes (list): The permission classes required for accessing this view.
    """

    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart_items = Cart.objects.filter(user=self.request.user).cart_items.all()
        serializer.save(user=self.request.user, order_items=cart_items)
        cart_items.delete()

class OrderDetailView(generics.RetrieveAPIView):
    """
    A view for retrieving, updating, and deleting an order.

    Inherits from generics.RetrieveAPIView and provides the following methods:
    - get_object: Retrieves the order object and checks if the user has permission to access it.
    - get: Handles GET requests and retrieves the order.
    - put: Handles PUT requests and updates the order.
    - delete: Handles DELETE requests and deletes the order.
    - perform_update: Performs additional actions after updating the order.

    Attributes:
        queryset (QuerySet): The queryset used to retrieve the order.
        serializer_class (Serializer): The serializer class used for serializing the order.
        permission_classes (list): The permission classes required to access the view.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieves the order object and checks if the user has permission to access it.

        Returns:
            Order: The order object.

        Raises:
            PermissionDenied: If the user does not have permission to access the order.
        """
        order = super().get_object()
        if order.user != self.request.user:
            raise PermissionDenied()
        return order
    
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and retrieves the order.

        Args:
            request (HttpRequest): The HTTP request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The HTTP response containing the serialized order.
        """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        """
        Handles PUT requests and updates the order.

        Args:
            request (HttpRequest): The HTTP request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The HTTP response containing the serialized updated order.
        """
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        """
        Handles DELETE requests and deletes the order.

        Args:
            request (HttpRequest): The HTTP request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The HTTP response indicating the successful deletion of the order.
        """
        return self.destroy(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        """
        Performs additional actions after updating the order.

        Args:
            serializer (Serializer): The serializer used for updating the order.
        """
        serializer.save(user=self.request.user)

class OrderUpdateView(generics.UpdateAPIView):
    """
    A view for updating an Order instance.

    This view allows an admin user to update an Order instance by providing the necessary data.
    The updated Order instance will be saved with the current user as the user who performed the update.

    Inherits from generics.UpdateAPIView.
    """
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class OrderDeleteView(generics.DestroyAPIView):
    """
    A view for deleting an Order instance.

    Inherits from generics.DestroyAPIView, which provides the default implementation
    for deleting a model instance.

    Attributes:
        queryset (QuerySet): The queryset of Order objects.
        serializer_class (Serializer): The serializer class for Order objects.
        permission_classes (list): The list of permission classes for the view.

    Methods:
        delete(request, *args, **kwargs): Deletes the Order instance.
        perform_destroy(instance): Performs the actual deletion of the instance.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    def perform_destroy(self, instance):
        instance.delete()

class ChangeOrderStatusView(generics.UpdateAPIView):
    """
    A view for changing the status of an order by the Delivery Crew.

    This view allows users in the 'Delivery Crew' group to change the status of an order.
    The view expects the order ID and the new status as input.

    Attributes:
        queryset (QuerySet): The queryset used to retrieve the order.
        serializer_class (Serializer): The serializer class used for validating and deserializing the request data.
        permission_classes (list): The permission classes required to access the view.
    """
    queryset = Order.objects.all().filter(delivered=True)
    serializer_class = OrderStatusSerializer
    permission_classes = [IsDeliveryCrew]
    def put(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class AssignOrderView(generics.UpdateAPIView):
    """
    A view for assigning orders to the delivery group.

    This view allows users in the 'Manager' group to assign orders to the 'Delivery Crew' group.
    The view expects the order ID and the user ID of the delivery crew member as input.

        Attributes:
            queryset (QuerySet): The queryset used to retrieve the order.
                serializer_class (Serializer): The serializer class used for validating and deserializing the request data.
                permission_classes (list): The permission classes required to access the view.
    """
    queryset = Order.objects.all()
    serializer_class = AssignOrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]

    def put(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        user_id = request.data.get('user_id')

        order = self.get_object()
        user = get_object_or_404(User, id=user_id)

        if user.groups.filter(name='Delivery Crew').exists():
            order.delivery_crew = user
            order.save()
            return Response({'message': 'Order assigned successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid user ID or user is not in the Delivery Crew group.'}, status=status.HTTP_400_BAD_REQUEST)

class OrderItemListView(generics.ListAPIView):
    """
    A view for retrieving, creating, updating, and deleting order items.
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def get_queryset(self):
        return super().get_queryset()
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def put (self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderItemDetailView(generics.RetrieveAPIView):
    """
    A view for retrieving, updating, and deleting an order item.

    Inherits from `generics.RetrieveAPIView` and provides the following HTTP methods:
    - GET: Retrieves the order item.
    - PUT: Updates the order item.
    - DELETE: Deletes the order item.

    Requires the user to be an admin user.

    Overrides the `get_object` method to retrieve the order item.
    Overrides the `get`, `put`, and `delete` methods to handle the corresponding HTTP methods.
    Overrides the `perform_update` method to save the updated order item with the current user.
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        return super().get_object()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# Order management endpoints        
class OrderListView(generics.ListAPIView):
    """
    API view for listing and creating orders.
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

    def get_queryset(self):
        """
        Returns the queryset of orders filtered by the current user.
        """
        return Order.objects.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and returns a list of orders.
        """
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests and creates a new order.
        """
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        """
        Sets the user of the order to the current user before saving.
        """
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    """
    A view for retrieving, updating, and deleting an order.

    Inherits from `generics.RetrieveAPIView` and provides the following HTTP methods:
    - GET: Retrieve an order
    - PUT: Update an order
    - DELETE: Delete an order

    Only authenticated users are allowed to access this view.

    Attributes:
        queryset (QuerySet): The queryset of all orders.
        serializer_class (Serializer): The serializer class for the order model.
        permission_classes (list): The list of permission classes for this view.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        order = super().get_object()
        if order.user != self.request.user:
            raise PermissionDenied()
        return order
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Category management endpoints
class CategoryListView(generics.ListAPIView):
    """
    A view that returns a list of all categories.

    Inherits from `generics.ListAPIView` and uses the `CategorySerializer`
    to serialize the queryset of `Category` objects.

    Attributes:
        queryset (QuerySet): The queryset of `Category` objects.
        serializer_class (Serializer): The serializer class for `Category` objects.
        permission_classes (list): The list of permission classes for the view.
        ordering_fields (list): The list of fields that can be used for ordering the categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    ordering_fields = ['name']

class CategoryDetailView(generics.RetrieveAPIView):
    """
    A view for retrieving a single category.

    This view allows any user to retrieve a single category object.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class CategoryCreateView(generics.CreateAPIView):
    """
    View for creating a new category.

    This view allows an admin user to create a new category by sending a POST request
    with the required data. The category will be created and saved in the database.

    Endpoint: /api/categories/create/
    Method: POST
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryUpdateView(generics.UpdateAPIView):
    """
    A view for updating a Category instance.

    This view allows an admin user to update a Category instance by sending a PATCH or PUT request
    to the specified endpoint. The updated data should be provided in the request body in a format
    that can be deserialized by the CategorySerializer.

    Only admin users are allowed to access this view.

    Endpoint: /api/categories/<pk>/update/
    Methods: PATCH, PUT
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryDeleteView(generics.DestroyAPIView):
    """
    A view for deleting a Category instance.

    Inherits from generics.DestroyAPIView, which provides the default implementation
    for deleting an object.

    Attributes:
        queryset (QuerySet): The queryset of Category objects.
        serializer_class (Serializer): The serializer class for Category objects.
        permission_classes (list): The list of permission classes for the view.

    Methods:
        delete(request, *args, **kwargs): Deletes the Category instance.
        perform_destroy(instance): Performs the actual deletion of the instance.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    def perform_destroy(self, instance):
        instance.delete()

class ChangeFeaturedItemView(generics.UpdateAPIView):
    """
    A view for changing the featured item of the day.

    This view allows the manager group to update the featured item of the day
    by sending a PUT request to the specified endpoint. The updated featured item
    should be provided in the request body in a format that can be deserialized by
    the MenuItemSerializer.

    Only users in the manager group are allowed to access this view.

    Endpoint: /api/featured-item/update/
    Method: PUT
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]

    def put(self, request, *args, **kwargs):
        featured_item = get_object_or_404(MenuItem, featured=True)
        serializer = self.get_serializer(featured_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)