from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_descriptions = models.CharField(max_length=255)
    product_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # abstract = True
        ordering = ['-id']

    def __str__(self):
        return self.product_name
