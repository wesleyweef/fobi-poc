from django.contrib import admin
from .models import Dados


@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    list_display = ["email", 'created_at']
