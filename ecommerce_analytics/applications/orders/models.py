from django.db import models

# Create your models here.

class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    website_session_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    primary_product_id = models.PositiveSmallIntegerField()
    items_purchased = models.PositiveSmallIntegerField()
    price_usd = models.DecimalField(max_digits=6, decimal_places=2)
    cogs_usd = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'orders'

class OrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    order_id = models.PositiveBigIntegerField()
    product_id = models.PositiveSmallIntegerField()
    is_primary_item = models.PositiveSmallIntegerField()
    price_usd = models.DecimalField(max_digits=6, decimal_places=2)
    cogs_usd = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_items'

class OrderItemRefunds(models.Model):
    order_item_refund_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    order_item_id = models.PositiveBigIntegerField()
    order_id = models.PositiveBigIntegerField()
    refund_amount_usd = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_item_refunds'