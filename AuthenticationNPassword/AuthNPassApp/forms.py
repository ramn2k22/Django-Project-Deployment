from django import forms
from django.contrib.auth.models import User
from AuthNPassApp.models import UserProfileInfo

# class UserForm(forms.ModelForm):

#     password=forms.CharField(widget=forms.PasswordInput())

#     class Meta():

#         model=User
#         fields=('username','email','password')

# class UserProfileInfoForms(forms.ModelForm):
#     class Meta():

#         model=UserProfileInfo
#         fields=('portfolia_site','profile_pic')


class UserForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model=User
        fields=('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):


    class Meta():

        model=UserProfileInfo
        fields=('portfolio_site', 'profile_pic')