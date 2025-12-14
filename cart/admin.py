from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    autocomplete_fields = ("book",)
    readonly_fields = ("subtotal",)

    def subtotal(self, obj):
        if obj.book:
            return obj.book.price * obj.quantity
        return 0
    subtotal.short_description = "Subtotal"


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "item_count", "total_quantity")
    search_fields = ("user__username", "user__email")
    inlines = [CartItemInline]

    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = "Distinct items"

    def total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())
    total_quantity.short_description = "Total quantity"