from django.views import generic
from django.contrib.auth.models import User

# from django.contrib.auth import login, logout
# from django.contrib.auth.views import LoginView
# from django.shortcuts import resolve_url, redirect


# Create your views here.

# User list view
class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'