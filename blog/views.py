from django.urls import reverse
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from .models import Category, Post
from .forms import CategoryForm


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
    success_message = 'The Category has been Created Successfully.'


# Update Category
class CategoryUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Category
    template_name = 'backend/category_create.html'
    form_class = CategoryForm
    success_message = 'The Category has been Updated Successfully.'

    def get_success_url(self):
        return reverse('category_update', kwargs={'pk': self.object.pk})


# Delete Category
class CategoryDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Category
    success_url = '/blog/categories/'
    template_name = 'common/delete.html'
    success_message = 'Successfully Deleted'

#create post list
class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'backend/post_list.html'

#create new post