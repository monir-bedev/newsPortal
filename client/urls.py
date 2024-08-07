from django.urls import path
from . import views

urlpatterns = [
    path('', views.FrontPageTemplateView.as_view(), name='home'),
    path('post/detail/<pk>/', views.DetailPageView.as_view(), name='post_details'),
]
