from django import forms
from . models import CustomUser, HistoryModel

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

class AddHistoryForm(forms.ModelForm):
    class Meta:
        model = HistoryModel
        fields = ['numberOfDonate','location_place', 'patient_contract', 'date']
        
class UpdateHistoryForm(forms.ModelForm):
    class Meta:
        model = HistoryModel
        fields = ['numberOfDonate','location_place', 'patient_contract']

        