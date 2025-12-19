from modeltranslation.translator import translator, TranslationOptions
from .models import TeamMember

class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('nickname', 'position', 'description')

translator.register(TeamMember, TeamMemberTranslationOptions)
