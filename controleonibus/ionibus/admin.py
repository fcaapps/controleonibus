from django.contrib import admin
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao
from django.contrib.admin.models import LogEntry

class EventoAdmin(admin.ModelAdmin):
    model = Eventos
    date_hierarchy = 'criado_em'
    list_display = ('tipo', 'circuito', 'parte','data_evento', 'texto_base', 'criado_em', 'atualizado_em')
    list_filter = ('tipo', 'data_evento')
    search_fields = ('tipo', 'circuito', 'parte','data_evento')    

class CongregacaoAdmin(admin.ModelAdmin):
    model = Congregacao
    date_hierarchy = 'criado_em'
    list_display = ('nome','coordenador','tel_coordenador','email_coordenador','criado_em', 'atualizado_em')
    search_fields = ('nome', 'coordenador', 'email_coordenador')
    list_per_page = 3;    

    # def get_actions(self, request):
    #     actions = super(CongregacaoAdmin, self).get_actions(request)
    #     if request.user.username[0].upper() != 'J':
    #         del actions['delete_selected']
    #     return actions


admin.site.register(Eventos, EventoAdmin)
admin.site.register(Congregacao, CongregacaoAdmin)
admin.site.site_header = 'iOnibus - Painel Administrativo'







