from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView

def oiDjango(request):
    return HttpResponse('Ola primeiro app')

urlpatterns=[
    path('olaApp/', oiDjango),
    path('cadastrar_pessoa/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('lista_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
]