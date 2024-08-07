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
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="blog/thumbnails", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

# Crete Posts Model
class Post(DomainEntity):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/%Y/%m/%d")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


# Create Comments Model
class Comment(DomainEntity):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment{} by{}'.format(self.name, self.body)