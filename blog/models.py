from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# core template domain entety

class DomainEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create category models

class Category(DomainEntity):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="blog/thumbnails", blank=True, null=True)

    def __str__(self):
        return self.name

# Create Post models

class Post(DomainEntity):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/%Y/%m/%d")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

# Create comment models

class Comment(DomainEntity):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
