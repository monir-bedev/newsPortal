from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,PostListView


urlpatterns = [
    # Category list
    path('categories/', CategoryListView.as_view(), name='category_list'),
    
    # Create new category
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),

    # Update category
    path('update-category/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),

    # Delete category
    path('delete-category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

    # Post List
    path('post-list/', PostListView.as_view(), name='post_list'),
]