from django.contrib import admin
from .models import Mensagem, Categoria, Tag

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criada_em")
    list_filter = ("categoria", "tags")
    search_fields = ("titulo", "conteudo")
    filter_horizontal = ("tags", )
