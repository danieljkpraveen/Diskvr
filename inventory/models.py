import uuid
from django.db import models
from django.contrib.auth.models import User


class NeonLights(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.ImageField(
        upload_to='inventory_images',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255)
    price = models.FloatField(
        blank=True,
        null=True
    )
    inches = models.CharField(max_length=255)
    ip_rating = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    led_lights_used = models.IntegerField(
        blank=True,
        null=True
    )
    sheet_mm = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='neon_lights',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Neon Lights'
    
    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = [
        ('NA', 'Not accepted'),
        ('IP', 'In progress'),
        ('CO', 'Complete'),
    ]

    order_id = models.CharField(
        max_length=36,
        primary_key=True,
        editable=False
    )
    product_name = models.CharField(
        max_length=255,
        editable=False
    )
    price = models.FloatField(
        null=True,
        blank=True
    )
    product_image_path = models.CharField(
        max_length=255,
        editable=False
    )
    username = models.CharField(
        max_length=150,
        editable=False
    )
    email = models.EmailField(editable=False)
    phone_number = models.CharField(
        max_length=15,
        editable=False
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='NA',
    )

    def __str__(self):
        return self.order_id
