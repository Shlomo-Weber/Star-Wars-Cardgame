from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput())
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput())

# class ProfileForm(forms.Form):
#     name = forms.CharField(max_length=60)
#     species = forms.ChoiceField()