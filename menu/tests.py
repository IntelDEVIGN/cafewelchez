import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Restaurante, Categoria, Item
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_restaurante(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["lugar"] = "lugar"
    defaults["activo"] = "activo"
    defaults["texto_menu"] = "texto_menu"
    defaults.update(**kwargs)
    return Restaurante.objects.create(**defaults)


def create_categoria(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["activa"] = "activa"
    defaults["mask_height"] = "mask_height"
    defaults["header_price_1"] = "header_price_1"
    defaults["header_price_2"] = "header_price_2"
    defaults.update(**kwargs)
    if "restaurante" not in defaults:
        defaults["restaurante"] = create_restaurante()
    return Categoria.objects.create(**defaults)


def create_item(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["descripcion"] = "descripcion"
    defaults["precio"] = "precio"
    defaults["precio_2"] = "precio_2"
    defaults["activo"] = "activo"
    defaults.update(**kwargs)
    if "categoria" not in defaults:
        defaults["categoria"] = create_categoria()
    return Item.objects.create(**defaults)


class RestauranteViewTest(unittest.TestCase):
    '''
    Tests for Restaurante
    '''
    def setUp(self):
        self.client = Client()

    def test_list_restaurante(self):
        url = reverse('menu_restaurante_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_restaurante(self):
        url = reverse('menu_restaurante_create')
        data = {
            "nombre": "nombre",
            "lugar": "lugar",
            "activo": "activo",
            "texto_menu": "texto_menu",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_restaurante(self):
        restaurante = create_restaurante()
        url = reverse('menu_restaurante_detail', args=[restaurante.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_restaurante(self):
        restaurante = create_restaurante()
        data = {
            "nombre": "nombre",
            "lugar": "lugar",
            "activo": "activo",
            "texto_menu": "texto_menu",
        }
        url = reverse('menu_restaurante_update', args=[restaurante.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CategoriaViewTest(unittest.TestCase):
    '''
    Tests for Categoria
    '''
    def setUp(self):
        self.client = Client()

    def test_list_categoria(self):
        url = reverse('menu_categoria_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_categoria(self):
        url = reverse('menu_categoria_create')
        data = {
            "nombre": "nombre",
            "activa": "activa",
            "mask_height": "mask_height",
            "header_price_1": "header_price_1",
            "header_price_2": "header_price_2",
            "restaurante": create_restaurante().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_categoria(self):
        categoria = create_categoria()
        url = reverse('menu_categoria_detail', args=[categoria.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_categoria(self):
        categoria = create_categoria()
        data = {
            "nombre": "nombre",
            "activa": "activa",
            "mask_height": "mask_height",
            "header_price_1": "header_price_1",
            "header_price_2": "header_price_2",
            "restaurante": create_restaurante().pk,
        }
        url = reverse('menu_categoria_update', args=[categoria.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ItemViewTest(unittest.TestCase):
    '''
    Tests for Item
    '''
    def setUp(self):
        self.client = Client()

    def test_list_item(self):
        url = reverse('menu_item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        url = reverse('menu_item_create')
        data = {
            "nombre": "nombre",
            "descripcion": "descripcion",
            "precio": "precio",
            "precio_2": "precio_2",
            "activo": "activo",
            "categoria": create_categoria().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_item(self):
        item = create_item()
        url = reverse('menu_item_detail', args=[item.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_item(self):
        item = create_item()
        data = {
            "nombre": "nombre",
            "descripcion": "descripcion",
            "precio": "precio",
            "precio_2": "precio_2",
            "activo": "activo",
            "categoria": create_categoria().pk,
        }
        url = reverse('menu_item_update', args=[item.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


