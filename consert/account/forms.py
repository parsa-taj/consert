from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

# how to register forms when using customUser(using abstractUser)
class UserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', "avatar", ]

# we can use UserChangeForm instead
class ProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email","avatar")
