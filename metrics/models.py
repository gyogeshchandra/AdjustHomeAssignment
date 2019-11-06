from django.db import models

class Metric(models.Model):
        date = models.DateField(auto_now=False, auto_now_add=False)
        channel = models.CharField(max_length=50)
        country = models.CharField(max_length=2)
        os = models.CharField(max_length=20)
        impressions = models.IntegerField(default=0)
        clicks = models.IntegerField(default=0)
        installs = models.IntegerField(default=0)
        spend = models.DecimalField(max_digits=10, decimal_places=2)
        revenue = models.DecimalField(max_digits=10, decimal_places=2)
