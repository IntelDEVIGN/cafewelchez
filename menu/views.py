from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Restaurante, Categoria, Item
from .forms import RestauranteForm, CategoriaForm, ItemForm


def indice(request):
    """
    :param request:
    :return: Listado de Restaurantes
    """

    restaurantes = Restaurante.objects.all()
    return render(request, "menu/index.html", {'restaurantes': restaurantes})


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

    def form_valid(self, form):
        categoria = form.save(commit=False)
        restaurante_id = form.data['restaurante']
        restaurante = get_object_or_404(Restaurante, id=restaurante_id)
        categoria.restaurante = restaurante
        return super(CategoriaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CategoriaCreateView, self).get_context_data(**kwargs)
        context['r_id'] = self.kwargs['restaurante_id']
        return context

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = self.object.restaurante.slug
        return reverse('menu_restaurante_detail', kwargs={'slug': slug})


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

    def form_valid(self, form):
        item = form.save(commit=False)
        categoria_id = form.data['categoria']
        categoria = get_object_or_404(Categoria, id=categoria_id)
        item.categoria = categoria
        return super(ItemCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['c_id'] = self.kwargs['categoria_id']
        return context

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = self.object.categoria.slug
        return reverse('menu_categoria_detail', kwargs={'slug': slug})


class ItemDetailView(DetailView):
    model = Item


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
