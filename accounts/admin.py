from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email','image']

admin.site.register(CustomUser, CustomUserAdmin)
