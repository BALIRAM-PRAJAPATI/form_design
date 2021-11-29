from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from django.db.models.lookups import In
from django.forms import widgets
from .models import Incident
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'email': 'Email'}

class EditUserProfileForm(UserChangeForm):
 password = None
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
  labels = {'email': 'Email'}

class EditAdminProfileForm(UserChangeForm):
 password = None
 class Meta:
  model = User
  fields = '__all__'
  labels = {'email': 'Email'}
#incident form
class IncidentForm(forms.Form):  
    LOCATION_CHOICES =(
    ("Carporate Headffice", "Carporate Headffice"),
    ("Operations Department", "Operations Department"),
    ("Work Station", "Work Station"),
    ("Marketing Division", "Marketing Division"),    
    ) 
    severity_choice = (
      ("Mild", "Mild"),
      ("Moderate", "Moderate"),
      ("severe", "severe"),
      ("Fatal", "Fatal"),
    )
    OPTIONS = (
        ("Enviormental Incident", "Enviormental Incident"),
        ("Injury/Illness", "Injury/Illness"),
        ("Property Damage", "Property Damage"),
        ("Vehicle", "Vehicle"),
    )     
    
    location = forms.ChoiceField(choices=LOCATION_CHOICES)
    incident_department = forms.CharField(max_length=100)   
    initial_severity = forms.ChoiceField(choices=severity_choice)    
    #subincident_types = forms.CharField(max_length=100)
    subincident_types = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)