from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'senha']
