from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput

from .models import Episode, EpisodeQueen


class EpisodeQueenInline(admin.StackedInline):
    model = EpisodeQueen
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }


class EpisodeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }
    inlines = (EpisodeQueenInline,)
    list_display = ('episode_long_name', 'air_date')
    ordering = ['season', 'episode_number']


admin.site.register(Episode, EpisodeAdmin)

