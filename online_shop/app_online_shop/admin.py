from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from static import *

class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_time', 'auction', 'get_html_photo']
    list_filter = ['auction', 'created_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    # photo = models.ImageField(upload_to='static/img/adv.png', blank=True, null=True)
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'), 
            'classes': ['collapse']
        })
    )
    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        else:
            return mark_safe(f"<img src='adv.png' width=50>")

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

admin.site.register(OnlineShop, OnlineShopAdmin)

