from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, Review, Item, Serviceable_list_items

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name','is_published','list_date',)
    exclude=('location',)

admin.site.register(Review)
admin.site.register(Item)
admin.site.register(Serviceable_list_items)
