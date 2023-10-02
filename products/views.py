from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'