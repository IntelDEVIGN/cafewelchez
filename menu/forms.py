from django import forms
from django.forms import Textarea
from material import Layout, Row

from .models import Restaurante, Categoria, Item


class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'lugar', 'activo', 'texto_menu']
        widgets = {
            'texto_menu': Textarea(attrs={'cols': 80, 'rows': 5})
        }

    layout = Layout('nombre',
                    Row('lugar', 'activo'),
                    'texto_menu')


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'activa', 'mask_height', 'header_price_1', 'header_price_2', 'restaurante']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'descripcion', 'precio', 'precio_2', 'activo', 'categoria']

