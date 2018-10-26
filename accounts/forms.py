from django.contrib.auth.forms import UserCreationForm
from django import forms
from localflavor.br.forms import BRCPFField, BRZipCodeField

from .models import User

class UserAdminCreationForm(UserCreationForm):

    cpf = BRCPFField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'cpf', 'gender', 'telephone', 'birth']

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']
