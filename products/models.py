from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    number = models.IntegerField()
    address=models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self) -> str:
        return f"{self.name} "

