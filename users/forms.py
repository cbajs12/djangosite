from django import forms
from django.contrib.auth import get_user_model

class JoinForm(forms.ModelForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(),max_length=128)
	country = forms.CharField(required=False)
	comment = forms.CharField(required=False)
	last_login = forms.DateField()

	class Meta:
		model = get_user_model()
		fields = ('first_name','last_name', 'email', 'password','last_login','country','comment')

class ChangeForm(forms.ModelForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput(),max_length=128)
	country = forms.CharField(required=False)
	comment = forms.CharField(required=False)

	class Meta:
		model = get_user_model()
		fields = ('first_name','last_name', 'password','country','comment')
