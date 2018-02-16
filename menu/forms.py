from django import forms
from django.forms import Textarea
from material import Layout, Row

from .models import Restaurante, Categoria, Item


class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['orden', 'nombre', 'lugar', 'activo', 'texto_menu']
        widgets = {
            'texto_menu': Textarea(attrs={'cols': 40, 'rows': 2})
        }

    layout = Layout(Row('orden', 'activo'),
                    'nombre', 'lugar',
                    'texto_menu')


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['orden', 'nombre', 'activa', 'mask_height', 'header_price_1', 'header_price_2']
        exclude = ['restaurante']

    layout = Layout(Row('orden', 'activa'),
                    'nombre',
                    Row('mask_height', 'header_price_1', 'header_price_2'))


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['orden', 'nombre', 'nivel', 'descripcion', 'precio', 'precio_2', 'activo']
        exclude = ['categoria']

    layout = Layout(Row('orden', 'activo'),
                    'nombre', 'descripcion',
                    Row('nivel', 'precio', 'precio_2'))

