from django import forms
from . models import CustomUser

class CustomForms(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'bloodgroup', 'donateStatus', 
                  'district','subdistrict', 'union', 'contract', 'image']


class UserLogInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    class Meta:
        fields = ['username', 'password']


class CustomUpdateForms(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email','password', 'bloodgroup', 'donateStatus', 
                  'district','subdistrict', 'union', 'contract', 'image']
        