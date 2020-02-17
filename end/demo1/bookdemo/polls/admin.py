from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.

from .models import VoteInfo,VoteOption

class VoteOptionInline(admin.StackedInline):
    model = VoteOption
    extra = 2

class VoteInfoAdmin(ModelAdmin):

    list_display = ('vote_title',)
    inlines = [VoteOptionInline]

class VoteOptionAdmin(ModelAdmin):
    list_display = ('content',)

admin.site.register(VoteInfo,VoteInfoAdmin)
admin.site.register(VoteOption,VoteOptionAdmin)