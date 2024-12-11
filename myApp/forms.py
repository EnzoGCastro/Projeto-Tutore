from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=False, min_value=0)
    university_major = forms.CharField(max_length=100, required=False)
    university_of_origin = forms.CharField(max_length=100, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'age',
            'university_major',
            'university_of_origin',
            'profile_picture',
        )