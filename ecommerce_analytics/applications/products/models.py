from django.db import models

# Create your models here.

class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    product_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'products'