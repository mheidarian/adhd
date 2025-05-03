from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'date_of_birth', 'phone_number']
        labels = {
            'image': 'تصویر',
            'bio': 'درباره من',
            'date_of_birth': 'تاریخ تولد',
            'phone_number': 'شماره تلفن',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        } 