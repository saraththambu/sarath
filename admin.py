from django.contrib import admin
from.models import Products
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name','price','stock')



# Register your models here.
admin.site.register(Products,ProductAdmin)
