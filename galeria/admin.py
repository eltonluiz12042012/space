from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

@admin.register(Fotografia)
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'legenda','categoria', 'foto','data_fotografia' ,'publicada', )
    list_display_links = ('id','nome',)
    fields =  ('nome', 'legenda','categoria',  'descricao', 'foto', 'publicada','data_fotografia')
    list_per_page = 10
    list_filter = ('categoria',)
    search_fields = ('nome', 'legenda')
    list_editable = ('publicada',)
    #ordering = ('id','nome')