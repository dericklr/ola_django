from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDetailView, PessoaDeleteView, CategoriaCreateView, CategoriaDeleteView, CategoriaListView, CategoriaUpdateView, CategoriaDetailView, ReceitaCreateView,ReceitaDetailView, ReceitaListView,ReceitaUpdateView,ReceitaDeleteView

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
    path('deletar_pessoa/<int:pk>/',PessoaDeleteView.as_view(), name='deletar_pessoa'),
    path('categorias/<int:pk>editar/', CategoriaUpdateView.as_view(),name='editar_categoria'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='detalhe_categoria'),
    path('listar_categorias/', CategoriaListView.as_view(), name='listar_categorias'),
    path('deletar_categoria/<int:pk>/', CategoriaDeleteView.as_view(), name='deletar_categoria'),
    path('cadastrar_categoria/', CategoriaCreateView.as_view(), name='cadastrar_categoria'),
    path('categoria_receitas/', ReceitaCreateView.as_view(), name='categoria_receitas'),
    path('cat_receitas/<int:pk>editar/', ReceitaUpdateView.as_view(),name='editar_receita'),
    path('cat_receitas/<int:pk>/', ReceitaDetailView.as_view(), name='detalhe_receita'),
    path('listar_receitas/', ReceitaListView.as_view(), name='listar_receita'),
    path('deletar_receita/<int:pk>/', ReceitaDeleteView.as_view(), name='deletar_receita'),



]
