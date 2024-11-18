from django import forms
from .models import Pessoa, CategoriaDespesas, CategoriasReceitas 

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

class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields='__all__'

class FormDeletePessoa(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields=[]                

class CategoriaDespesasForm(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields='__all__'

class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields='__all__'


class FormDeleteCategorias(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields=[]

class CategoriaReceitaForm(forms.ModelForm):
    class Meta:
        model=CategoriasReceitas
        fields='__all__'

class ReceitaUpdateForm(forms.ModelForm):
    class Meta:
        model=CategoriasReceitas
        fields='__all__'        

class FormDeleteReceita(forms.ModelForm):
    class Meta:
        model=CategoriasReceitas
        fields=[]
