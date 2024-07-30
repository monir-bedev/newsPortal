from django.views import generic
from .models import Category
from .forms import CategoryForm

# Create your views here.

# Category List

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'backend/category_list.html'


# Create New Category List

class CategoryCreateView(generic.CreateView):
    model = Category
    success_url = '/blog/category/create/'
    template_name = 'backend/category_create.html'
    form_class = CategoryForm
