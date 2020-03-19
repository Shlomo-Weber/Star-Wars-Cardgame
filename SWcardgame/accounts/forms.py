from django import forms
from django.forms import ModelForm
from .models import Profile
class SignupForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput())
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
