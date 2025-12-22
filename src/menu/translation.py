from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Subcategory, MenuItem

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class MenuItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Category, CategoryTranslationOptions)
translator.register(Subcategory, SubcategoryTranslationOptions)
translator.register(MenuItem, MenuItemTranslationOptions)
