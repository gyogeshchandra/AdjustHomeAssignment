from django_filters import rest_framework as rest_framework_filters
from .models import Metric
from django_filters.filters import BaseInFilter, CharFilter

class CharInFilter(BaseInFilter,CharFilter):
        pass

class MetricFilter(rest_framework_filters.FilterSet):
        date = rest_framework_filters.DateFromToRangeFilter()
        channel = CharInFilter(lookup_expr='in')
        os = CharInFilter(lookup_expr='in')
        country = CharInFilter(lookup_expr='in')

        class Meta:
                model = Metric
                fields = ('date','channel','country','os')
