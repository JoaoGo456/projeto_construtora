from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Colaborador

@admin.register(Colaborador) 

class ColaboradorAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'matricula', 'cargo', 'ativo') 
    search_fields = ('nome', 'matricula')

