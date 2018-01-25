from django import forms
from .models import Restaurante, Categoria, Item


class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'lugar', 'activo', 'texto_menu']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'activa', 'mask_height', 'header_price_1', 'header_price_2', 'restaurante']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'descripcion', 'precio', 'precio_2', 'activo', 'categoria']


