from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import TeamMember
import pages.translation

@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('order', 'nickname', 'position')
    list_editable = ('order',)
    list_display_links = ('nickname',)
    ordering = ('order',)
