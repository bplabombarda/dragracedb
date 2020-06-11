from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput

from .models import Season


class SeasonAdmin(admin.ModelAdmin):
    fields = ('name', 'season_number', 'season_type',)
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }
    list_display = ('name',)
    ordering = ['season_type', 'season_number',]


admin.site.register(Season, SeasonAdmin)
