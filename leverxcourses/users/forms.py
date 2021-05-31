# from django.conf import settings
# from django.contrib.auth.forms import UserCreationForm
#
# User = settings.AUTH_USER_MODEL
# from django.forms import ModelForm, TextInput, DateInput, FileInput, Select, FileField, Textarea, EmailField, CharField
#
#
# class SignUpForm(UserCreationForm):
#     first_name = CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = CharField(max_length=30, required=False, help_text='Optional.')
#     email = EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups')
