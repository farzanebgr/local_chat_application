from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name',
                                 widget=forms.TextInput(attrs={
                                     'class':'form-control form-control-lg'}),
                                 validators=[validators.MaxLengthValidator(50),])
    last_name = forms.CharField(label='Last name',
                                widget=forms.TextInput(attrs={
                                    'class':'form-control form-control-lg'}),
                                validators=[validators.MaxLengthValidator(50),])
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control form-control-lg'}),
                               validators=[validators.MaxLengthValidator(50),])
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'class':'form-control form-control-lg'}),
                               validators=[validators.MaxLengthValidator(100),])
    phone = forms.CharField(label='Phone',
                             widget=forms.TextInput(attrs={
                                 'class':'form-control form-control-lg'}),)
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                 'class':'form-control form-control-lg'}),
                             validators=[validators.MaxLengthValidator(100),
                                         validators.EmailValidator,])
    user_avatar = forms.ImageField()
    user_gender = forms.BooleanField(label='Lady')


class LoginForm(forms.Form):
        username = forms.CharField(
            label='Username',
            widget=forms.TextInput(attrs={
                                 'class':'form-control form-control-lg'}),
            validators=[
                validators.MaxLengthValidator(100),
            ]
        )
        password = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(attrs={
                                 'class':'form-control form-control-lg'}),
            validators=[
                validators.MaxLengthValidator(100)
            ]
        )
