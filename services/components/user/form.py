from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': _('Username')}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'placeholder': _('Password')
        }
    ))
