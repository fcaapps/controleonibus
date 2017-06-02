from django.contrib import admin
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao
from controleonibus.ionibus.models import Circuito
from controleonibus.ionibus.models import Responsavel
from controleonibus.ionibus.models import Capitao
from controleonibus.ionibus.models import Passageiro
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
    list_display = ('nome','coordenador', 'endereco', 'tel_coordenador','email_coordenador','circuito')
    list_filter = ('circuito','criado_em')
    search_fields = ('nome', 'coordenador', 'endereco', 'email_coordenador','circuito')
    list_per_page = 10;    

class ResponsavelAdmin(admin.ModelAdmin):
    model = Responsavel
    date_hierarchy = 'criado_em'
    list_display = ('nome','tipo','congregacao','email','telefone')
    list_filter = ('congregacao','tipo')
    search_fields = ('foto','nome','tipo','congregacao','email','telefone')
    list_per_page = 10;    

class CapitaoAdmin(admin.ModelAdmin):
    model = Capitao
    date_hierarchy = 'criado_em'
    list_display = ('nome','congregacao','telefone1','telefone2')
    list_filter = ('congregacao','criado_em')
    search_fields = ('nome','congregacao','telefone1','telefone2')
    list_per_page = 10;    

class PassageiroAdmin(admin.ModelAdmin):
    model = Passageiro
    date_hierarchy = 'criado_em'
    list_display = ('nome','congregacao','rg_cpf','capitao','crianca_colo')
    list_filter = ('congregacao','capitao')
    search_fields = ('nome','congregacao','rg_cpf','capitao','crianca_colo')
    list_per_page = 10;    


admin.site.register(Eventos, EventoAdmin)
admin.site.register(Congregacao, CongregacaoAdmin)
admin.site.register(Circuito, CircuitoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(Capitao, CapitaoAdmin)
admin.site.register(Passageiro, PassageiroAdmin)
admin.site.site_header = 'iOnibus - Painel Administrativo'

