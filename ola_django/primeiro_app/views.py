from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Pessoa
from .forms import PessoaForm, PessoaUpdateForm, FormDeletePessoa
from django.urls import reverse_lazy


class PessoaCreateView(CreateView):
    model=Pessoa
    from_class=PessoaForm
    template_name='cadastrar_pessoa.html'
    success_url=reverse_lazy('lista_pessoa')

class PessoaListView(ListView):
    model= Pessoa
    template_name='lista_pessoas.html'

class PessoaUpdateView(UpdateView):
    model=Pessoa
    template_name='cadastrar_pessoa.html'
    form_class=PessoaUpdateForm
    success_url=reverse_lazy('lista_pessoas')


class PessoaDetailView(DetailView):
    model=Pessoa
    template_name='detalhe_pessoa.html'

class PessoaDeleteView(DeleteView):
    model=Pessoa
    form_class=FormDeletePessoa
    template_name='deletar_pessoa.html'
    success_url=reverse_lazy('lista_pessoas')  

# Create your views here.
