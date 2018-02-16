from django.contrib import admin
from django import forms
from .models import Restaurante, Categoria, Item


def regrabar(modeladmin, request, queryset):
    for objeto in queryset:
        objeto.creado = '2018-01-20'
        objeto.save()


regrabar.short_description = "Regrabar"


class RestauranteAdminForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = '__all__'


class RestauranteAdmin(admin.ModelAdmin):
    actions = [regrabar]
    form = RestauranteAdminForm
    list_display = ['orden', 'nombre', 'activo', 'lugar', 'platos', 'texto_menu', 'slug', 'creado',
                    'actualizado']
    readonly_fields = ['platos', 'slug', 'creado', 'actualizado']


admin.site.register(Restaurante, RestauranteAdmin)


class CategoriaAdminForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class CategoriaAdmin(admin.ModelAdmin):
    actions = [regrabar]
    form = CategoriaAdminForm
    list_display = ['orden', 'nombre', 'activa', 'mask_height', 'header_price_1', 'header_price_2', 'platos', 'slug',
                    'creada', 'actualizada']
    readonly_fields = ['platos', 'slug', 'creada', 'actualizada']


admin.site.register(Categoria, CategoriaAdmin)


class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    actions = [regrabar]
    form = ItemAdminForm
    list_display = ['orden', 'nombre', 'activo', 'descripcion', 'precio', 'precio_2', 'slug', 'creado', 'actualizado']
    readonly_fields = ['slug', 'creado', 'actualizado']


admin.site.register(Item, ItemAdmin)
