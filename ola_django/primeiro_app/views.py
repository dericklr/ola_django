from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from models import Pessoa
from forms import PessoaForm
from django.urls import reverse_lazy


class PessoaCreateView(CreateView):
    model=Pessoa
    from_class=PessoaForm
    template_name='cadastrar_pessoa.html'
    success_url=reverse_lazy('lista_pessoa')

class PessoaListView(ListView):
    model= Pessoa
    template_name='lista_pessoas.html'

# Create your views here.
