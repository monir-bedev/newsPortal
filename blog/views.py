from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .models import Category
from .forms import CategoryForm

# Create your views here.

# Category List

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'backend/category_list.html'


# Create New Category List

class CategoryCreateView(SuccessMessageMixin, generic.CreateView):
    model = Category
    success_url = '/blog/category/create/'
    template_name = 'backend/category_create.html'
    form_class = CategoryForm
    success_message = 'The Category has been successfully Created.'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super(CategoryCreateView, self).form_valid(form)


# Update Category

class CategoryUpdateView(generic.UpdateView):
    model = Category
    success_url = '/blog/categories/'
    template_name = 'backend/category_create.html'
    form_class = CategoryForm