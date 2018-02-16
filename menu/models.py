from django.core.urlresolvers import reverse
from django.db.models.functions import Coalesce
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Restaurante(models.Model):

    # Fields
    orden = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    lugar = models.CharField(max_length=100)
    texto_menu = models.TextField(max_length=255)
    platos = models.IntegerField(null=True, blank=True)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True, overwrite=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('orden',)
        verbose_name_plural = 'Restaurantes'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    @property
    def count_platos(self):
        if self.categorias.exists():
            count_agregado = self.categorias.aggregate(items=Sum('platos'))
            return count_agregado['items']
        else:
            return 0

    def save(self, *args, **kwargs):
        self.platos = self.count_platos
        super(Restaurante, self).save()

    def get_absolute_url(self):
        return reverse('menu_restaurante_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('menu_restaurante_update', args=(self.slug,))


class Categoria(models.Model):

    # Fields
    orden = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=100)
    activa = models.BooleanField(default=True)
    mask_height = models.IntegerField(null=True, blank=True)
    header_price_1 = models.TextField(max_length=100, null=True, blank=True)
    header_price_2 = models.TextField(max_length=100, null=True, blank=True)
    platos = models.IntegerField(null=True, blank=True)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True, overwrite=True)
    creada = models.DateTimeField(auto_now_add=True, editable=False)
    actualizada = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    restaurante = models.ForeignKey('menu.Restaurante', on_delete=CASCADE, related_name='categorias')

    class Meta:
        ordering = ('orden',)
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.restaurante.nombre + ' - ' + self.nombre

    def __unicode__(self):
        return u'%s' % self.restaurante.nombre + ' - ' + self.nombre

    @property
    def count_platos(self):
        if self.items.exists():
            count_items = self.items.count()
            return count_items
        else:
            return 0

    def save(self, *args, **kwargs):
        elrestaurante = Restaurante.objects.get(id=self.restaurante.pk)
        self.platos = self.count_platos
        super(Categoria, self).save()
        elrestaurante.save()

    def get_absolute_url(self):
        return reverse('menu_categoria_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('menu_categoria_update', args=(self.slug,))


class Item(models.Model):

    # Fields
    orden = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True, default=" ")
    nivel = models.IntegerField(null=True, blank=True, default=1)
    precio = models.IntegerField(null=True, blank=True, default=None)
    precio_2 = models.IntegerField(null=True, blank=True, default=None)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True, overwrite=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    actualizado = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    # Relationship Fields
    categoria = models.ForeignKey('menu.Categoria', on_delete=CASCADE, related_name='items')

    class Meta:
        ordering = ('orden',)
        verbose_name = 'Ítem'
        verbose_name_plural = 'Ítems'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    @property
    def restaurante(self):
        return self.categoria.restaurante.nombre

    def save(self, *args, **kwargs):
        lacategoria = Categoria.objects.get(id=self.categoria.pk)
        if self.precio == 0:
            self.precio = None
        if self.precio_2 == 0:
            self.precio_2 = None
        super(Item, self).save()
        lacategoria.save()

    def get_absolute_url(self):
        return reverse('menu_item_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('menu_item_update', args=(self.slug,))
