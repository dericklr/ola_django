from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDetailView, PessoaDeleteView

def oiDjango(request):
    return HttpResponse('primeiro app')

urlpatterns=[
    path('olaApp/', oiDjango),
    path('cadastrar_pessoa/',PessoaCreateView.as_view(),name='cadastrar_pessoa'),
    path('listar_pessoas/', PessoaListView.as_view(), name='listar_pessoas'),
    path('pessoas/<int:pk>editar/', PessoaUpdateView.as_view(),name='editar_pessoa'),
    path('pessoas/<int:pk>/',PessoaDetailView.as_view(), name='detalhe_pessoa'),
    path('deletar_pessoa/<int:pk>/',PessoaDeleteView.as_view(), name='deletar_pessoa'),

]
