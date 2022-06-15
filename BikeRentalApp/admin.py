from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","contact","address","avatar")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("type","image")

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("category","company","model_name","colour","booked","vehicle_status","image")

@admin.register(RentVehicle)
class RentVehicleAdmin(admin.ModelAdmin):
    list_display = ("user","vehicle","renttype","duration","license","rented_at")

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ("rented_vehicle","total_bill","bill_status")

admin.site.register(Payment)


