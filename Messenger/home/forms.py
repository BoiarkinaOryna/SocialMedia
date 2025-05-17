from django import forms
from .models import User_Post

class UserPostForm(forms.ModelForm):
    class Meta:
        model = User_Post
        fields = ['title', 'theme', 'content', 'tags', 'link']#, 'images']
        widgets = {
            'title': forms.TextInput(attrs = {
                'placeholder': 'Напишіть заголовок публікації'
            }),
            'theme': forms.TextInput(attrs = {
                'placeholder': 'Напишіть тему публікації',
            }),
            'content': forms.Textarea(attrs = {
                'placeholder': 'Напишіть тему публікації',
            }),
            'link': forms.URLInput(attrs = {
                'placeholder': 'Вставьте посилання',
            })
        }
        labels = {
            'title': 'Назва публікації',
            'theme': 'Тема публікації',
            'content': '',
            'tags': '',
            'link': 'Посилання'
        }

class ChangeUserPostForm(forms.ModelForm):
    class Meta:
        model = User_Post
        fields = ['title', 'theme', 'content', 'tags', 'link']#, 'images']
        widgets = {
            'title': forms.TextInput(attrs = {
                'placeholder': 'Напишіть заголовок публікації'
            }),
            'theme': forms.TextInput(attrs = {
                'placeholder': 'Напишіть тему публікації',
            }),
            'content': forms.Textarea(attrs = {
                'placeholder': 'Напишіть тему публікації',
            }),
            'link': forms.URLInput(attrs = {
                'placeholder': 'Вставьте посилання',
            })
        }
        labels = {
            'title': 'Назва публікації',
            'theme': 'Тема публікації',
            'content': '',
            'tags': '',
            'link': 'Посилання'
        }