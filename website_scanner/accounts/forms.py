from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        fields = ('username','fname','lname','email','password1','password2')
        model = CustomUser # using custom user model for Signup form