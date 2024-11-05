from django.urls import path
from django.http import HttpResponse
<<<<<<< HEAD
from .views import PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDetailView, PessoaDeleteView, CategoriaView, CategoriaDeleteView, CategoriaListView, CategoriaUpdateView, CategoriaDetailView
=======
from .views import CategoriaDetailView, CategoriaListView, CategoriaUpdateView, PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDetailView, PessoaDeleteView, CategoriaCreateView
>>>>>>> a8f3bd1c98808b5d62bf027961296369efe5f884

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
<<<<<<< HEAD
    path('categorias/', CategoriaView.as_view(), name='categoria_despesas'),
    path('categorias/<int:pk>editar/', CategoriaUpdateView.as_view(),name='editar_categoria'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='detalhe_categoria'),
    path('listar_categorias/', CategoriaListView.as_view(), name='listar_categorias'),
    path('deletar_categoria/<int:pk>/', CategoriaDeleteView.as_view(), name='deletar_categoria')

=======
    path('cadastrar_categoria/', CategoriaCreateView.as_view(), name='cadastrar_categoria'),
>>>>>>> a8f3bd1c98808b5d62bf027961296369efe5f884
]
