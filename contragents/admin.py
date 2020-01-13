from django.contrib import admin

from contragents.models import Contragent


@admin.register(Contragent)
class ContragentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'email', 'phone']
