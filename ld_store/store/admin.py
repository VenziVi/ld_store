from django.contrib import admin
from django.db.models import Count
from . models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'products_count']
    search_fields = ['name'] # used by product autocompete
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(ordering='products_count')
    def products_count(self, category):
        return category.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )
    
class InventoryFilter(admin.SimpleListFilter): # Custom filter
    title = 'quantity'
    parameter_name = 'quantity'
    low_qty_value = 3

    def lookups(self, request, model_admin):
        return [
            ('<low_qty_value', 'Low qty')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '<low_qty_value':
            return queryset.filter(quantity__lt=self.low_qty_value)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']
    actions = ['clear_quantity']
    list_display = ['title', 'category', 'price', 'quantity_status']
    list_editable = ['price']
    list_per_page = 10
    list_filter = ['category', InventoryFilter]
    search_fields = ['title__istartswith']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(ordering='quantity') # orderin for quantity_status
    def quantity_status(self, product):
        if not product.quantity:
            return 'Out of Stock'
        elif product.quantity < 3:
            return "Low qty"
        return "OK"

    @admin.action(description='Clear quantity')
    def clear_quantity(self, request, queryset):
        updated_count = queryset.update(quantity=0)
        self.message_user(
            request,
            f'{updated_count} products where updated.'
        )