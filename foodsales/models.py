from django.db import models

# Create your models here.


class restItem(models.Model):
     OrderDate=models.DateTimeField(auto_now_add=True)
     Region=models.CharField(max_length=10)
     City=models.CharField(max_length=10)
     Category=models.CharField(max_length=10)
     Product=models.CharField(max_length=10)
     Quantity=models.IntegerField()
     UnitPrice=models.FloatField(max_length=10)

     def __str__(self):
        return self.Product
