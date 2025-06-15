from django import forms
from .models import User_Post
from registration.models import Profile

TAG_CHOICES = [
    (1, '#відпочинок'),
    (2, '#натхнення'),
    (3, '#життя'),
    (4, '#природа'),
    (5, '#читання'),
    (6, '#спокій'),
    (7, '#гармонія'),
    (8, '#музика'),
    (9, '#фільми'),
    (10, '#подорожі'),
]
class UserPostForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(
        choices = TAG_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={
            'class': 'tag-div'
        }),
        label = '',
        required = False,
    )
    
    class Meta:
        model = User_Post
        fields = ['title', 'theme', 'content', 'tags', 'link']
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
            }),
        }
        labels = {
            'title': 'Назва публікації',
            'theme': 'Тема публікації',
            'content': '',
            'link': 'Посилання'
        }
        

class ChangeUserPostForm(forms.ModelForm):
    class Meta:
        model = User_Post
        fields = ['title', 'theme', 'content', 'tags', 'link']
        widgets = {
            'title': forms.TextInput(attrs = {
                'placeholder': 'Змініть заголовок публікації'
            }),
            'theme': forms.TextInput(attrs = {
                'placeholder': 'Змініть тему публікації',
            }),
            'content': forms.Textarea(attrs = {
                'placeholder': 'Змініть тему публікації',
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

class FirstEditInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "username"]
        labels = {
            "first_name": "Ім'я",
            "last_name": "Прізвище",
            "username": "Ім'я користувача",
        }
        widgets = {
            "first_name": forms.TextInput(attrs = {
                "placeholder": "Введіть Ваше ім’я"
            }),
            "last_name": forms.TextInput(attrs = {
                "placeholder": "Введіть Ваше прізвище"
            }),
            "username": forms.TextInput(attrs = {
                "value": "@"
            }),
        }