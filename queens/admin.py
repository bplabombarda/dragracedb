from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput

from .models import Queen


class QueenAdmin(admin.ModelAdmin):
    fields = ('name', 'home_city', 'home_state', 'home_country',)
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }
    list_display = ('name', 'home_city', 'home_state', 'home_country')
    ordering = ['name']


admin.site.register(Queen, QueenAdmin)
