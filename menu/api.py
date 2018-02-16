from . import models
from . import serializers
from rest_framework import viewsets, permissions


class RestauranteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Restaurante class"""

    queryset = models.Restaurante.objects.all()
    serializer_class = serializers.RestauranteSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_fields = ('id',)


class CategoriaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Categoria class"""

    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_fields = ('restaurante',)


class ItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the Item class"""

    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_fields = ('categoria',)