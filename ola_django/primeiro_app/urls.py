from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDetailView, PessoaDeleteView

def oiDjango(request):
    return HttpResponse('Ola primeiro app')

urlpatterns=[
    path('olaApp/', oiDjango),
    path('cadastrar_pessoa/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('lista_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
    path('pessoas<int:pk>;editar/', PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('pessoas/<int:pk>/', PessoaDetailView.as_view(), name='detalhe_pessoa'),
    path('deletar_pessoas/<int:pk>/', PessoaDeleteView.as_view(), name='deletar_pessoa'),

]