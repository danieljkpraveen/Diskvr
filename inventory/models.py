from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='inventory_items',
        on_delete=models.CASCADE
    )
    price = models.FloatField()
    image = models.ImageField(upload_to='inventory_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='inventory_items',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Inventory'

    def __str__(self):
        return self.name