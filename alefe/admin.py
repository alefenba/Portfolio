from django.contrib import admin
from .models import Categoria, Habilidades, Inicio, Perfil, Projeto, Sobre, Certificado


# Inicio
admin.site.register(Inicio)


# About
class ProfileInline(admin.TabularInline):
    model = Perfil
    extra = 1

@admin.register(Sobre)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Habilidades
    extra = 2

@admin.register(Categoria)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Projeto
admin.site.register(Projeto)


# Projeto
admin.site.register(Certificado)