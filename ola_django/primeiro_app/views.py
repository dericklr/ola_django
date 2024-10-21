from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Pessoa, InteracoesPessoa, CategoriaDespesas
from .forms import PessoaCreateForm, PessoaUpdateForm,FormDeletePessoa, CategoriaDespesasForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class PessoaCreateView(CreateView):
    model=Pessoa
    form_class=PessoaCreateForm
    template_name='cadastrar_pessoa.html'
    success_url=reverse_lazy('listar_pessoas')

    def form_valid(self, form):
            response=super().form_valid(form)

            InteracoesPessoa.objects.create(
                  pessoa= self.object,
                  mensagem=form.cleaned_data['interacao']
                  )  
            messages.success(self.request,'Pessoa cadastrada com sucesso')
            return response

class PessoaListView(ListView):
        model= Pessoa
        template_name='listar_pessoas.html'

class PessoaUpdateView(UpdateView):
      model= Pessoa
      template_name='editar_pessoa.html'
      form_class=PessoaUpdateForm
      success_url=reverse_lazy('listar_pessoas')

      def form_valid(self, form):
            response= super().form_valid(form)
            if (form.cleaned_data['interacao']!=''):
                  InteracoesPessoa.objects.create(
                        pessoa=self.object,
                        mensagem=form.cleaned_data['interacao']
                  )

            messages.success(self.request,'Pessoa cadastrada com sucesso')
            return response
            
class PessoaDetailView(DetailView):
      model=Pessoa
      template_name='detalhe_pessoa.html' 

      def get_context_data(self, **kwargs):
            context= super().get_context_data(**kwargs)
            pessoa=self.object  
            interacoes=InteracoesPessoa.objects.filter(pessoa=pessoa)
            interacoes_formatada=[{
                  'data_hora': interacao.data_hora.strftime('%d/%m/%Y %H:%M'),
                  'mensagem' : interacao.mensagem
                  }
                  for interacao in interacoes
            ]
            context['interacoes_formatada']= interacoes_formatada   
            return context

class PessoaDeleteView(DeleteView):
      model= Pessoa
      form_class=FormDeletePessoa
      template_name='deletar_pessoa.html'
      success_url=reverse_lazy('listar_pessoas')



class CategoriaView(CreateView):
    model= CategoriaDespesas
    form_class=CategoriaDespesasForm
    template_name='categoria_despesas.html'
    success_url=reverse_lazy('listar_pessoas')
