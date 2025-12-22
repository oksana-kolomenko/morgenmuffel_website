from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from menu.models import Category, Subcategory, MenuItem
import menu.translation

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Subcategory)
class SubcategoryAdmin(TranslationAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(TranslationAdmin):
    list_display = ('name', 'subcategory', 'price')
    list_filter = ('subcategory', 'subcategory__category')
    search_fields = ('name', 'description')
