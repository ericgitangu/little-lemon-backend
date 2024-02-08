from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = '__all__'
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)

class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.
    """
    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    """
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def retrieve(self, validated_data):
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating an order.
    """

    class Meta:
        model = Order
        fields = '__all__'

    
    def create(self, validated_data):
        """
        Create a new order.

        Args:
            validated_data (dict): The validated data for creating the order.

        Returns:
            Order: The created order instance.
        """
        # Set the customer group for the order
        validated_data['customer_group'] = 'customer'
        return super().create(validated_data)


class OrderUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating an OrderItem instance.

    This serializer provides methods for creating, retrieving, updating, and deleting an OrderItem.
    It also provides methods for getting field names, fields, default field names, unique together constraints,
    and extra kwargs.

    Usage:
    serializer = OrderUpdateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    """

    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def retrieve (self, validated_data):
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderItem model.
    """
    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def retrieve (self, validated_data):
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def retrieve (self, validated_data):
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()
class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        return super().create(validated_data)

    def retrieve (self, validated_data):
        return super().retrieve(validated_data)

    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()

class UserLogoutSerializer(serializers.ModelSerializer):
    """
    Serializer for logging out a user.
    """
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def retrieve (self, validated_data):
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()

class AssignOrderSerializer(serializers.ModelSerializer):
    """
    Serializer for assigning an order to a delivery crew.
    """
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def retrieve (self, validated_data):
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()
    
class OrderStatusSerializer(serializers.ModelSerializer):
    """
    Serializer for updating the status of an Order instance.
    """
    class Meta:
        model = Order
        fields = ['status']

    def update(self, instance, validated_data):
        instance.status = True
        instance.save()
        return instance
    

class ChangeFeaturedItemSerializer(serializers.ModelSerializer):
    """
    Serializer for changing the featured item.
    """
    class Meta:
        model = MenuItem
        fields = ['featured']

    def update(self, instance, validated_data):
        instance.featured = True
        instance.save()
        return instance

class DeliveryCrewUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the DeliveryCrewUser model.
    """
    class Meta:
        model = DeliveryCrewUser
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
    
    def retrieve (self, validated_data):
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()
    
class UserTokenSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserToken model.
    """
    class Meta:
        model = UserToken
        fields = '__all__'
        
    def create(self, validated_data):
        return super().create(validated_data)
        
    def retrieve(self, validated_data):
        return super().retrieve(validated_data)
        
    def delete(self, validated_data):
        return super().delete(validated_data)
        
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
        
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
        
    def get_fields(self):
        return super().get_fields()
        
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
        
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)
        
    def get_extra_kwargs(self):
        return super().get_extra_kwargs()