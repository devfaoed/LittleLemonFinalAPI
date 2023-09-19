from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoryView.as_view(), name="category"),
    path('menu-item', views.MenuItemView.as_view(), name="menu-items"),
    path('cart', views.CartView.as_view(), name="cart items"),
    path('order', views.OrderView.as_view(), name="orders"),
    path('order-item', views.orderItemViews.as_view(), name="orders items"),
]
