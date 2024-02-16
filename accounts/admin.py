from django.contrib import admin
from .models import CustomUser, HistoryModel

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email','image']

admin.site.register(CustomUser, CustomUserAdmin)

class HistoryModelAdmin(admin.ModelAdmin):
    model = HistoryModel
    list_display = ['user', 'numberOfDonate', 'location_place', 'patient_contract', 'date']

admin.site.register(HistoryModel, HistoryModelAdmin)
