from django.contrib import admin
from car_brand_app.models import Brand

# Register your models here.
class BrandName_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand_name',)}
    list_display = ['brand_name','slug']

admin.site.register(Brand,BrandName_admin)
