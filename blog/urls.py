from django.urls import path
from . import views


urlpatterns = [
    # Category list
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    
    # Create new category
    path('create-category/', views.CategoryCreateView.as_view(), name='category_create'),

    # Update category
    path('update-category/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),

    # Delete category
    path('delete-category/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),

    # Post List
    path('posts/', views.PostListView.as_view(), name='post_list'),

    # New post Create
    path('create-post/', views.CreatePostView.as_view(), name='post_create'),

    # Update post
    path('update-post/<int:pk>/', views.UpdatePostView.as_view(), name='post_update'),

    # Delete post
    path('delete-post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),

]