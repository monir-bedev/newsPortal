from django.urls import path
from . import views


urlpatterns = [
   path('users/', views.UserListView.as_view(), name='users'),
   path('create-user/', views.CreateUserView.as_view(), name='create_user'),
   path('update-user/<int:pk>/', views.UserUpdateView.as_view(), name='update_user'),
   path('delete-user/<int:pk>/', views.DeleteUserView.as_view(), name='delete_user'),

]