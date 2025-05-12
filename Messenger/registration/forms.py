from django import forms
from .models import Profile


# Треба було використовувати ModelForm, а не просто Form
class UserForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs = {
                'placeholder': 'you@example.com',
                # 'class': 
            }),
            'password': forms.TextInput(attrs = {
                'placeholder': 'Введи пароль',
                'type': 'password'
            })
        }
        labels = {
            'email': 'Електронна пошта',
            'password': 'Пароль'
        }

class AuthUserForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['email', 'password']