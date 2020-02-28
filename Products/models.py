from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
