from django.contrib import admin

from store.models import Product, ProductGallery, ReviewRating, Variation
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

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
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)