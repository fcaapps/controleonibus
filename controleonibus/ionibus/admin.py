from django.contrib import admin
from controleonibus.ionibus.models import Eventos

class EventoAdmin(admin.ModelAdmin):
    model = Eventos
    date_hierarchy = 'criado_em'
    list_display = ('id','tipo', 'circuito', 'parte','data_evento', 'texto_base', 'criado_em', 'atualizado_em')
    # list_filter = ('tipo', 'data_evento', 'texto_base', 'criado_em', 'atualizado_em')
    search_fields = ('tipo', 'circuito', 'parte','data_evento')
    # exclude = ['texto_base']

admin.site.register(Eventos, EventoAdmin)





