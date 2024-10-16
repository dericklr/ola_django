from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields='__all__'


class PessoaUpdateForm(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields='__all__'

class FormDeletePessoa(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields=[]
                
        