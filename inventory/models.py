from django.db import models
from django.contrib.auth.models import User


class NeonLights(models.Model):
    image = models.ImageField(upload_to='inventory_images', blank=True, null=True)
    name = models.CharField(max_length=255)
    inches = models.CharField(max_length=255)
    ip_rating = models.CharField(max_length=150, blank=True, null=True)
    led_lights_used = models.IntegerField(blank=True, null=True)
    sheet_mm = models.CharField(max_length=100, blank=True, null=True)
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
