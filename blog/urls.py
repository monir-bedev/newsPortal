from django.urls import path
from .views import CategoryListView


urlpatterns = [
    # All category list
    path('categories/', CategoryListView.as_view(), name='category_list'),
]