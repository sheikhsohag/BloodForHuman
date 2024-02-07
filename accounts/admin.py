from django.contrib import admin
from .models import CustomUser

# Register your models here.

admin.site.register(CustomUser)

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email']

