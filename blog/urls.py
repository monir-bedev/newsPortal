from django.urls import path
from .views import CategoryListView, CategoryCreateView


urlpatterns = [
    # All category list
    
    path('categories/', CategoryListView.as_view(), name='category_list'),
    
    # Create new category

    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]