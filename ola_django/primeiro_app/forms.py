from django import forms
from .models import Pessoa, CategoriaDespesas

class PessoaCreateForm(forms.ModelForm):
    interacao=forms.CharField(widget=forms.Textarea)
    class Meta:
        model= Pessoa
        fields='__all__'

class PessoaUpdateForm(forms.ModelForm):
    interacao=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Pessoa
        fields='__all__'

class FormDeletePessoa(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields=[]                

class CategoriaDespesasForm(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields='__all__'
