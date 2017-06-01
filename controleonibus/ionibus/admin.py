from django.contrib import admin
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao
from controleonibus.ionibus.models import Circuito
from controleonibus.ionibus.models import Responsavel
from django.contrib.admin.models import LogEntry

class CircuitoAdmin(admin.ModelAdmin):
    model = Circuito
    date_hierarchy = 'criado_em'
    list_display = ('nome','sigla','parte')
    search_fields = ('nome','sigla','parte')
    list_per_page = 10;    

class EventoAdmin(admin.ModelAdmin):
    model = Eventos
    date_hierarchy = 'criado_em'
    list_display = ('tipo', 'circuito', 'data_evento', 'texto_base')
    list_filter = ('tipo', 'circuito')
    search_fields = ('tipo', 'circuito','data_evento')    
    list_per_page = 10;

class CongregacaoAdmin(admin.ModelAdmin):
    model = Congregacao
    date_hierarchy = 'criado_em'
    list_display = ('nome','coordenador','tel_coordenador','email_coordenador','circuito', 'encarregado')
    list_filter = ('circuito','criado_em')
    search_fields = ('nome', 'coordenador', 'email_coordenador','circuito', 'encarregado')
    list_per_page = 10;    

class ResponsavelAdmin(admin.ModelAdmin):
    model = Responsavel
    date_hierarchy = 'criado_em'
    list_display = ('nome','tipo','congregacao','email','telefone')
    list_filter = ('congregacao','tipo')
    search_fields = ('foto','nome','tipo','congregacao','email','telefone')
    list_per_page = 10;    


admin.site.register(Eventos, EventoAdmin)
admin.site.register(Congregacao, CongregacaoAdmin)
admin.site.register(Circuito, CircuitoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.site_header = 'iOnibus - Painel Administrativo'







