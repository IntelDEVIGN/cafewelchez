from django.urls import include, path
from rest_framework import routers

from . import api, views

# from material.frontend import urls as frontend_urls

router = routers.DefaultRouter()
router.register(r'restaurante', api.RestauranteViewSet)
router.register(r'categoria', api.CategoriaViewSet)
router.register(r'item', api.ItemViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Restaurante
    path('restaurante/', views.RestauranteListView.as_view(), name='menu_restaurante_list'),
    path('restaurante/crear/', views.RestauranteCreateView.as_view(), name='menu_restaurante_create'),
    path('restaurante/detalle/<slug:slug>/', views.RestauranteDetailView.as_view(), name='menu_restaurante_detail'),
    path('restaurante/editar/<slug:slug>/', views.RestauranteUpdateView.as_view(), name='menu_restaurante_update'),
)

urlpatterns += (
    # urls for Categoria
    path('categoria/', views.CategoriaListView.as_view(), name='menu_categoria_list'),
    path('categoria/crear/<int:restaurante_id>/', views.CategoriaCreateView.as_view(), name='menu_categoria_create'),
    path('categoria/detalle/<slug:slug>/', views.CategoriaDetailView.as_view(), name='menu_categoria_detail'),
    path('categoria/editar/<slug:slug>/', views.CategoriaUpdateView.as_view(), name='menu_categoria_update'),
)

urlpatterns += (
    # urls for Item
    path('item/', views.ItemListView.as_view(), name='menu_item_list'),
    path('item/crear/<int:categoria_id>/', views.ItemCreateView.as_view(), name='menu_item_create'),
    path('item/detalle/<slug:slug>/', views.ItemDetailView.as_view(), name='menu_item_detail'),
    path('item/editar/<slug:slug>/', views.ItemUpdateView.as_view(), name='menu_item_update'),
)
