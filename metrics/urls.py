from django.urls import path
from .views import MetricList

urlpatterns = [
        path('metrics/',
                MetricList.as_view(), name='metric-list')
]
