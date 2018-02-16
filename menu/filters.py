from django.contrib.auth.models import User
from django.contrib.admin.filters import RelatedFieldListFilter, AllValuesFieldListFilter
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username':    ['exact', ],
            'first_name':  ['icontains', ],
            'last_name':   ['exact', ],
            'date_joined': ['year', 'year__gt', 'year__lt', ],
        }


class DropdownFilterValues(AllValuesFieldListFilter):
    template = 'admin/dropdown_filter.html'


class DropdownFilterRelated(RelatedFieldListFilter):
    template = 'admin/dropdown_filter.html'
