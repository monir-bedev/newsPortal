from django import forms
from .models import Category

# Create Category Form

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'thumbnail']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }