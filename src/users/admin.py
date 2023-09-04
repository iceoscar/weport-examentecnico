from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'qr_code')
    fields = ('first_name', 'last_name', 'username', 'type_blood', 'curp', 'photo', 'is_rrhh')
