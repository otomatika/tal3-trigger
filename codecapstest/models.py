from django.db import models

# Create your models here.


class testModel(models.Model):
    testField = models.CharField(max_length=50)
    testField2 = models.DecimalField(default=0, decimal_places=5, max_digits=20)