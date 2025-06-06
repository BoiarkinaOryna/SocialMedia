from django import forms
from registration.models import Profile

class EditInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "birthday", "email", "password"]
        labels = {
            "first_name": "Ім'я",
            "last_name": "Прізвище",
            "birthday": "Дата народження",
            "email": "Електронна адреса",
            "password": "Пароль"
        }
        widgets = {
            "first_name": forms.TextInput(attrs = {
                "placeholder": "Lina"
            }),
            "last_name": forms.TextInput(attrs = {
                "placeholder": "Li"
            }),
            "birthday": forms.TextInput(attrs = {
                "placeholder": "2001-09-10"
            }),
            "email": forms.TextInput(attrs = {
                "placeholder": "you@example.com"
            }),
            "password": forms.TextInput(attrs = {
                "placeholder": "⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕"
            })
        }
        error_messages = {
            'birthday': {
                'invalid': 'Ця дата не є валідною. Спробуйте формат 2000-01-01'
            }
        }