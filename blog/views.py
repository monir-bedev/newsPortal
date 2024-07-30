from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from .models import Category

# Create your views here.

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'backend/category_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        print("Hello World")
        return super().get_queryset()
