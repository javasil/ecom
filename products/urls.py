
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Product URLs
    path('', views.ProductListView.as_view(), name='product-list'),
    path('category/', views.CategoryListView.as_view(), name='category-list'),


]