from django.contrib import admin
from cars.models    import Car
from cars.models    import Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'licence_plate', 'value')
    search_fields = ('model', 'brand',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)