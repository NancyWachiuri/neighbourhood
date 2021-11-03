from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from .models import Profile,NeighbourHood,Business
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post',css_class = 'btn btn-warning'))

    class Meta:
        model = NeighbourHood
        fields = [
            'Name',
            'location',
            'population',
            'image',
            'healthno',
            'policeno'
            

        ]
        exclude =['user']


class BusinessForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post',css_class = 'btn btn-warning'))
    
    
    class Meta:
        model = Business
        fields = ['businessname','email','image','created_date']
        
            




