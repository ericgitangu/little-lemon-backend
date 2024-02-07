from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

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
    
    def retrieve (self, validated_data):
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        return super().delete(validated_data)
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)
    
    def get_fields(self):
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        return super().get_unique_together_constraints(model)

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
    Serializer for creating an order item.
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

class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the CartItem model.
    """
    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new CartItem instance.
        """
        return super().create(validated_data)
    
    def retrieve (self, validated_data):
        """
        Retrieve a CartItem instance.
        """
        return super().retrieve(validated_data)
    
    def delete(self, validated_data):
        """
        Delete a CartItem instance.
        """
        return super().delete(validated_data)
    
    def update(self, instance, validated_data):
        """
        Update a CartItem instance.
        """
        return super().update(instance, validated_data)
    
    def get_field_names(self, declared_fields, info):
        """
        Get the field names for the serializer.
        """
        return super().get_field_names(declared_fields, info)

    def get_fields(self):
        """
        Get the fields for the serializer.
        """
        return super().get_fields()
    
    def get_default_field_names(self, declared_fields, model_info):
        """
        Get the default field names for the serializer.
        """
        return super().get_default_field_names(declared_fields, model_info)
    
    def get_unique_together_constraints(self, model):
        """
        Get the unique together constraints for the serializer.
        """
        return super().get_unique_together_constraints(model)
    
    def get_extra_kwargs(self):
        """
        Get the extra keyword arguments for the serializer.
        """
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

class UserTokenSerializer(serializers.ModelSerializer):
    """
    Serializer for UserToken model.
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
        user = User.objects.create_user(**validated_data)
        return user
    
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