from django.contrib import admin

from store.models import Product, Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date')
    prepopulated_fields = {
        'slug': ('product_name',)
    }

class VariationAdmin(admin.ModelAdmin):
        list_display = ('product','variation_category','variation_value','is_active')
        list_editable = ('is_active',)
        list_filter =('product','variation_category','variation_value','is_active')

admin.site.register(Variation,VariationAdmin)
admin.site.register(Product,ProductAdmin)