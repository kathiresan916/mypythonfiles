from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)


class Expenses(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
