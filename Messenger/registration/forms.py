from django import forms
from .models import Profile


# Треба було використовувати ModelForm, а не просто Form
class UserForm(forms.ModelForm):
    password_confirmation = forms.CharField(
        required = True,
        label = "Підтверди пароль",
        widget = forms.TextInput(
            attrs = {"placeholder": "Повтори пароль", "type": "password"}
        )
    )
    class Meta():
        model = Profile
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs = {
                'placeholder': 'you@example.com',
                'email': ''
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
        widgets = {
            'email': forms.TextInput(attrs = {
                'placeholder': 'you@example.com',
                'email': ''
            }),
            'password': forms.TextInput(attrs = {
                'placeholder': 'Введи пароль',
                'type': 'password'
            })
        }