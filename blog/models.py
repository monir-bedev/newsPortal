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

    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

