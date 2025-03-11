from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email')
    list_filter = ('apellido',)
    search_fields = ('nombre', 'apellido', 'email')
    ordering = ('id',)