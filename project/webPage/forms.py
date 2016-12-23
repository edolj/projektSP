from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Naprava

class LoginForm(forms.Form):
	username = forms.CharField(label='Ime:', max_length=80)
	password = forms.CharField(label='Geslo', max_length=80, widget=forms.PasswordInput)
	
class UserForm(forms.ModelForm):
		password = forms.CharField(widget=forms.PasswordInput)
		
		class Meta:
			model = User
			fields = ['username','email','password']

			
class NapravaForm(forms.ModelForm):
		class Meta:
			model = Naprava
			fields = ['imeNaprave','opis','cena','picture','video']