from django.contrib.auth.models import User
from django import forms
from .models import ToDo
class UserForm(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
	class Meta:
		model=User
		fields=['username','email','password']

class LoginForm(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model=User
		fields=['username','password']

class TodoForm(forms.ModelForm):
	task=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="task")
	description=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="description")
	time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}),label="time")
	class Meta:
		model=ToDo
		fields=['task','description','time']