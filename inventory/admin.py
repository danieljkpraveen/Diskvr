from django.contrib import admin

from .models import NeonLights, Order


admin.site.register(NeonLights)


class OrderAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['order_id', 'product_name', 'product_image_path', 'username', 'email', 'phone_number']
        return []

admin.site.register(Order, OrderAdmin)