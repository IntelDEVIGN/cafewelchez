from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Restaurante, Categoria, Item
from .forms import RestauranteForm, CategoriaForm, ItemForm


class RestauranteListView(ListView):
    model = Restaurante


class RestauranteCreateView(CreateView):
    model = Restaurante
    form_class = RestauranteForm


class RestauranteDetailView(DetailView):
    model = Restaurante


class RestauranteUpdateView(UpdateView):
    model = Restaurante
    form_class = RestauranteForm


class CategoriaListView(ListView):
    model = Categoria


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm


class CategoriaDetailView(DetailView):
    model = Categoria


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm


class ItemListView(ListView):
    model = Item


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm


class ItemDetailView(DetailView):
    model = Item


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
