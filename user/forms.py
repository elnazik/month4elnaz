from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField( required=True)
    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password_confirm = cleaned_data.get('password_confirm')

        if password_confirm != cleaned_data.get('password_confirm'):
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)