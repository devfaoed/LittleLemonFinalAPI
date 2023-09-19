from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, menuItemSerializer, CartSerializer, OrderItemSerializer, OrderSerializers

# Create your views here.
# category view
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields  = ["title"]


# menu item view
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = menuItemSerializer
    ordering_fields = ["price"]
    filterset_fields  = ["price"]
    search_fields  = ["title"]

# cart view
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_permissions(self):
        if self.request.method == "GET" :
            return []
        
        return [IsAuthenticated()]

# order view
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def get_permissions(self):
        if self.request.method == "GET":
            return []

        return [IsAuthenticated()]


# order items view
class orderItemViews(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        
        return [IsAuthenticated()]

    