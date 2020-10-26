from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=128, blank=True, null=True)
    user_name = models.CharField(max_length=128, blank=True, null=True)
    user_comment = models.CharField(max_length=768, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCleaned(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_name = models.TextField(blank=True, null=True)
    user_name = models.TextField(blank=True, null=True)
    user_comment = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cleaned'