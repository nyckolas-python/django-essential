from django.contrib import admin
from .models import TV, Notebook, Dishwasher, Brand, Category, VacuumCleaner, Item, Promo


for model in [TV, Notebook, Category, VacuumCleaner, Promo]:
    admin.site.register(model)
class DishwasherInstanceInline(admin.TabularInline):
    model = Dishwasher


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [DishwasherInstanceInline]


@admin.register(Dishwasher)
class DishwasherAdmin(admin.ModelAdmin):
    class Media:
        css = {}

    list_display = ('model', 'brand_name', 'price',
                    'color', 'test_show_promo', 'colored_name')
    list_filter = ('price', 'brand_name', 'color',)
    fieldsets = (
        # separate section
        ('General info', {
            'classes': ('wide', 'extrapretty'),
            'description': ('The description of which is related to ' +
                            'General information'),
            'fields': ('brand_name', 'category', 'model',
                       'color', 'price', 'count', 'warranty'),
        }),
        # separate section
        ('Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'description': ('The description of which is related to ' +
                            'Advanced options'),
            'fields': ('power', 'width', 'height', 'energy_saving_class'),
        }),
        # separate section
        ('Other', {
            # 'collapse' - hidden (drop-down) block with fields
            'classes': ('collapse',),
            'description': ('The description of which is related to ' +
                            'Other'),
            'fields': ('description',),
        }),)
    sortable_by = 'price'
    search_fields = ['__all__']
    # exclude = ('price',)
    empty_value_display = '-Бренд відсутній-'
    # readonly_fields = ['price']

    def test_show_promo(self, obj):
        return obj.promo

    def delete_model(self, request, obj):
        pass
