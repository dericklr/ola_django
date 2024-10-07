from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields=['nome','idade','email']


class PessoaUpdateForm(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields='__all__'
        