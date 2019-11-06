from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics
from .filters import MetricFilter
from .serializers import MetricSerializer
from .models import Metric
from django.db.models import Sum,Avg,F,FloatField,ExpressionWrapper


class MetricList(generics.ListAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    #filter by functionality
    filterset_class = MetricFilter

    def get_queryset(self):
        queryset = self.queryset.extra(select={"cpi": "spend/installs"})
        columns = self.request.query_params.get("columns")
        group_by = self.request.query_params.get("group_by")
        sort_by = self.request.query_params.get("sort_by")
        order = self.request.query_params.get("order")
        fields = [field.name for field in Metric._meta.get_fields()]
        fields.append('cpi')



        #Group By functionality
        if group_by is not None:
        	valid_fields = ["date","channel","country","os"]
        	group_by = [value.strip() for value in group_by.split(",") if value.strip() in valid_fields]
        	if len(group_by) > 0:
        		aggregated_fields = ['impressions','clicks', 'installs', 'spend', 'revenue']
        		annotated_fields = { af: Sum(af) for  af in aggregated_fields }
        		annotated_fields['cpi'] = ExpressionWrapper(F('spend')/F('installs'), output_field=FloatField())
        		queryset = queryset.values(*group_by).\
        		annotate(**annotated_fields)

        #Sort By functionality
        if sort_by is not None:
            default_order = '-' if order == 'desc' else ''

            sort_by = [default_order+value.strip() for value in sort_by.split(",") if value.strip() in fields]
            if len(sort_by) > 0:
            	queryset = queryset.order_by(*sort_by)


        if columns is not None:
        	columns = [value.strip() for value in columns.split(",") if value.strip() in fields]
        	if group_by is not None:
        		columns = set(columns + group_by)
        	queryset = queryset.values(*columns)


        return queryset
