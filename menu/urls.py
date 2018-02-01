from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
# from material.frontend import urls as frontend_urls

router = routers.DefaultRouter()
router.register(r'restaurante', api.RestauranteViewSet)
router.register(r'categoria', api.CategoriaViewSet)
router.register(r'item', api.ItemViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns += (
    url(r'^schema/$', schema_view),
)

urlpatterns += (
    url(r'^docs/', include_docs_urls(title='API Menús Cafe Welchez')),
)
#
# urlpatterns += (
#     url(r'', include(frontend_urls)),
# )

urlpatterns += (
    # urls for Restaurante
    url(r'^restaurante/$', views.RestauranteListView.as_view(), name='menu_restaurante_list'),
    url(r'^restaurante/crear/$', views.RestauranteCreateView.as_view(), name='menu_restaurante_create'),
    url(r'^restaurante/detalle/(?P<slug>\S+)/$', views.RestauranteDetailView.as_view(), name='menu_restaurante_detail'),
    url(r'^restaurante/editar/(?P<slug>\S+)/$', views.RestauranteUpdateView.as_view(), name='menu_restaurante_update'),
)

urlpatterns += (
    # urls for Categoria
    url(r'^categoria/$', views.CategoriaListView.as_view(), name='menu_categoria_list'),
    url(r'^categoria/crear/(?P<restaurante_id>\d+)/$', views.CategoriaCreateView.as_view(), name='menu_categoria_create'),
    url(r'^categoria/detalle/(?P<slug>\S+)/$', views.CategoriaDetailView.as_view(), name='menu_categoria_detail'),
    url(r'^categoria/editar/(?P<slug>\S+)/$', views.CategoriaUpdateView.as_view(), name='menu_categoria_update'),
)

urlpatterns += (
    # urls for Item
    url(r'^item/$', views.ItemListView.as_view(), name='menu_item_list'),
    url(r'^item/crear/(?P<categoria_id>\d+)/$', views.ItemCreateView.as_view(), name='menu_item_create'),
    url(r'^item/detalle/(?P<slug>\S+)/$', views.ItemDetailView.as_view(), name='menu_item_detail'),
    url(r'^item/editar/(?P<slug>\S+)/$', views.ItemUpdateView.as_view(), name='menu_item_update'),
)
