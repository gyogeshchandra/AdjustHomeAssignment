from rest_framework import serializers
from .models import Metric

class MetricSerializer(serializers.ModelSerializer):
        date = serializers.DateField(required=False)
        channel = serializers.CharField(required=False)
        country = serializers.CharField(required=False)
        os = serializers.CharField(required=False)
        impressions = serializers.IntegerField(required=False)
        clicks = serializers.IntegerField(required=False)
        installs = serializers.IntegerField(required=False)
        spend = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
        revenue = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)


        class Meta:
                model = Metric
                fields = ("date","channel","country","os","impressions",
                "clicks","installs","spend","revenue")
