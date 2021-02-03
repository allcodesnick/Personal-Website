from django import forms
from .models import Company_Application

class Company_ApplicationForm(forms.ModelForm):
	class Meta:
		model = Company_Application
		fields = '__all__'