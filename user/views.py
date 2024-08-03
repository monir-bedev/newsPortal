from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse

from . forms import UserModelForm, UserProfileForm

# from django.contrib.auth.views import LoginView
# from django.contrib.auth import login, logout
# from django.shortcuts import resolve_url, redirect

# User list view
class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

# create a new user
class CreateUserView(generic.CreateView):
    model = User
    form_class = UserModelForm
    template_name = 'user_create.html'
    success_url = '/user/create-user/'

# update user
class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user_update.html'
    
    def get_success_url(self):
        return reverse('update_user', kwargs={'pk': self.object.pk})

# delete  user
class DeleteUserView(generic.DeleteView):
    model = User
    template_name = 'common/delete.html'
    success_url = '/user/users/'