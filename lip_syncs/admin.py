from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput

from .models import LipSync, LipSyncQueen


class LipSyncQueenInline(admin.StackedInline):
    model = LipSyncQueen
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }


class LipSyncAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }
    inlines = (LipSyncQueenInline,)
    list_display = ('episode', 'song', 'artist')
    ordering = ['episode', 'song', 'artist',]


admin.site.register(LipSync, LipSyncAdmin)
