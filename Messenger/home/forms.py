from django import forms
from .models import Post
from registration.models import User

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
        model = Post
        fields = ['title', 'tags', 'content']
        widgets = {
            'title': forms.TextInput(attrs = {
                'placeholder': 'Напишіть заголовок публікації'
            }),
            'content': forms.Textarea(attrs = {
                'placeholder': 'Напишіть тему публікації',
            }),
        }
        labels = {
            'title': 'Назва публікації',
            'content': '',
        }
        

class ChangeUserPostForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(
        choices = TAG_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={
            'class': 'tag-div'
        }),
        label = '',
        required = False,
    )
    class Meta:
        model = Post
        fields = ['title', 'tags', 'content']
        widgets = {
            'title': forms.TextInput(attrs = {
                'placeholder': 'Змініть заголовок публікації'
            }),
            'content': forms.Textarea(attrs = {
                'placeholder': 'Змініть тему публікації',
            }),
        }
        labels = {
            'title': 'Назва публікації',
            'content': '',
            'tags': ''
        }

class FirstEditInfoForm(forms.ModelForm):
    class Meta:
        model = User
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
        help_texts = {
               'username': None
           }