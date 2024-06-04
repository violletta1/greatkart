from django.contrib import admin

from orders.models import Order, OrderProduct, Payment

# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered','variations')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    readonly_fields = ['order_number', 'user','payment']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]
    
    
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'total_price','full_name')  # Clear and concise display
    readonly_fields = ('order','payment', 'user', 'product', 'quantity', 'product_price', 'ordered','variations')

    def total_price(self, obj):
        """Calculates and returns the total price for an OrderProduct instance."""
        return obj.quantity * obj.product_price
    
    def full_name(self, obj):
        """Retrieves the full name from the associated Order instance."""
        return obj.order

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)