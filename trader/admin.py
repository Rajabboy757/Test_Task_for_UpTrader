from django.contrib import admin

from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_main', 'parent')
    ordering = ['id']
    list_display_links = ('id', 'name')
    list_filter = ('is_main',)


admin.site.register(Menu, MenuAdmin)
