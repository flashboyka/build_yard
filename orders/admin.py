from django.contrib import admin

from orders import models
# Register your models here.


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
    list_display = ['number', 'price', 'created', 'edited']
