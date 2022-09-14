
# Register your models here.
from django.contrib import admin
from .models import Product

# admin.site.register(Product)
# admin potaldaki başlıkları falan değiştiriyor
admin.site.site_title = "Marcusway Title"
admin.site.site_header = "Marcusway Admin Portal"
admin.site.index_title = "Welcome to Marcusway Admin Portal"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ("is_in_stock",)
    # list_display_links = ("create_date", ) #can't add items in list_editable to here
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name",)
    search_fields = ("name",)
    # when adding product in admin site
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 25
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock") #fieldset kullandığımız zaman bunu kullanamayız

    fieldsets = (
        (None, {
            "fields": (
                # to display multiple fields on the same line, wrap those fields in their own tuple
                ('name', 'slug'), "is_in_stock"
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes": ("collapse", ),
            "fields": ("description",),
            'description': "You can use this section for optionals settings"
        })
    )


admin.site.register(Product, ProductAdmin)
