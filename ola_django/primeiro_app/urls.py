from django.urls import path
from django.http import HttpResponse
from .views import CategoriaDetailView, CategoriaListView, CategoriaUpdateView, PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDetailView, PessoaDeleteView, CategoriaCreateView

def oiDjango(request):
    return HttpResponse('primeiro app')

urlpatterns=[
    path('olaApp/', oiDjango),
    path('cadastrar_pessoa/',PessoaCreateView.as_view(),name='cadastrar_pessoa'),
    path('listar_pessoas/', PessoaListView.as_view(), name='listar_pessoas'),
    path('listar_categorias/', CategoriaListView.as_view(), name='listar_categorias'),
    path('pessoas/<int:pk>editar/', PessoaUpdateView.as_view(),name='editar_pessoa'),
    path('categorias/<int:pk>editar/', CategoriaUpdateView.as_view(),name='editar_categoria'),
    path('pessoas/<int:pk>/',PessoaDetailView.as_view(), name='detalhe_pessoa'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='detalhe_categoria'),
    path('deletar_pessoa/<int:pk>/',PessoaDeleteView.as_view(), name='deletar_pessoa'),
    path('cadastrar_categoria/', CategoriaCreateView.as_view(), name='cadastrar_categoria'),
]
