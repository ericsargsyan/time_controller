from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserRegisterForm(UserCreationForm):
	# email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'email']


class UserUpdateForm(forms.ModelForm):
	# email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username']


# class ProfileUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		# fields = ['image']
