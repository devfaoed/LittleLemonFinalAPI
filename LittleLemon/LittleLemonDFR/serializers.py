from rest_framework import serializers
from .models import Category, Cart, MenuItem, Order, OrderItem
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]


class menuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only = True)
    category = CategorySerializer(read_only = True)
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "featured", "category", "category_id" ]
        

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField( 
        queryset = User.objects.all(), 
        default = serializers.CurrentUserDefault() 
    )
    menuItems = menuItemSerializer(read_only = True)
    class Meta:
        model = Cart
        fields = ["id", "user", "menuItems", "quantity", "unit_price", "price"]
        validators = [
            UniqueTogetherValidator(
                queryset= Cart.objects.all(),
                fields=['user', 'menuItems']
            )
        ]

class OrderSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField( 
        queryset = User.objects.all(), 
        default = serializers.CurrentUserDefault() 
    )
    class Meta:
        model = Order
        fields = ["id", "user", "delivery_crew", "status", "total", "date"]

class OrderItemSerializer(serializers.ModelSerializer ):
    order_id = serializers.IntegerField(write_only = True)
    order = OrderSerializers(read_only = True)
    menuitems_id = serializers.IntegerField(write_only = True)
    menuitems = menuItemSerializer(read_only = True)
    class Meta:
        model = OrderItem
        fields = ["id", "order_id", "order", "menuitems_id", "menuitems", "quantity", "unit_price", "price"]
        validators = [
            UniqueTogetherValidator(
                queryset= Cart.objects.all(),
                fields=['order', 'menuItems']
            )
        ]

    



    