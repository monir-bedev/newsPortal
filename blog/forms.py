from django import forms
from .models import Category

# Create Category Form

class CategoryForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(CategoryForm, self)._init_(*args, **kwargs)
    #     self.fields['parent'].queryset = Category.objects.filter(parent='parent')

    class Meta:
        model = Category
        fields = ['name', 'thumbnail']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            # 'parent': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
