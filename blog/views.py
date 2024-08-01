from django.urls import reverse
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from .models import Category, Post
from .forms import CategoryForm, PostForm

# Category List
class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'backend/category_list.html'


# Create New Category List
class CategoryCreateView(SuccessMessageMixin, generic.CreateView):
    model = Category
    success_url = '/blog/create-category/'
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

# create post list
class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 20
    template_name = 'backend/post_list.html'

# create new post
class CreatePostView(SuccessMessageMixin, generic.CreateView):
    model = Post
    success_url = '/blog/create-post/'
    template_name = 'backend/post_create.html'
    form_class = PostForm
    success_message = 'The post has been created successfully.'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super(CreatePostView, self).form_valid(form)

# update post
class UpdatePostView(SuccessMessageMixin, generic.UpdateView):
    model = Post
    template_name = 'backend/post_create.html'
    form_class = PostForm
    success_message = 'The post has been Updated successfully.'

    def get_success_url(self):
        return reverse('post_update', kwargs={'pk': self.object.pk})


# delete post
class DeletePostView(SuccessMessageMixin, generic.DeleteView):
    model = Post
    success_url = '/blog/posts/'
    template_name = 'common/delete.html'
    success_message = 'Successfully Deleted'


# post details
class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'backend/post_details.html'

