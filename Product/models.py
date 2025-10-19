from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length = 70)
    product_price = models.IntegerField()
    product_count = models.SmallIntegerField()
    is_available = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now_add=True)



