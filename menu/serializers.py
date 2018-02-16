from . import models

from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = (
            'orden',
            'nombre',
            'descripcion',
            'nivel',
            'precio',
            'precio_2',
            'activo',
            'categoria',
            # 'slug',
            # 'creado',
            # 'actualizado',
        )
        # depth = 0


class CategoriaSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Categoria
        fields = (
            # 'id',
            # 'orden',
            'nombre',
            # 'restaurante',
            'items',
            'activa',
            'mask_height',
            'header_price_1',
            'header_price_2',
            # 'slug',
            # 'creada',
            # 'actualizada',
        )
        # depth = 1


class RestauranteSerializer(serializers.ModelSerializer):

    categorias = CategoriaSerializer(many=True, read_only=True)

    class Meta:
        model = models.Restaurante
        fields = (
            # 'id',
            # 'orden',
            'nombre',
            'categorias',
            'lugar',
            'activo',
            'texto_menu',
            # 'slug',
            # 'creado',
            # 'actualizado',
        )
        # depth = 5
