# forms.py
from django import forms

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
    ('O-', 'O-'),
]

class SearchForm(forms.Form):
    blood_group = forms.ChoiceField(label='Select blood group', choices=BLOOD_GROUP_CHOICES)
    location = forms.CharField(label='Enter Location', max_length=100)
