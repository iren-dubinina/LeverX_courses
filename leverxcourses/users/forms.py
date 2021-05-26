from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput


class RegistrationForm(ModelForm):
    class Meta:
        # model = User
        fields = ['name', 'date', 'group']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сourse name'
            }),
            "date": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start date'
            })
        }
