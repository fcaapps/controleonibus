from django.conf.urls import url, include

from controleonibus.ionibus import views

urlpatterns = [
    # Tela Principal
    url(r'^painel/$', views.painel, name="painel"),
    # Telas de Cadastro
    url(r'^cadastro_eventos/$', views.eventos_cadastro, name="eventos_cadastro"),
    url(r'^cadastro_congregacao/$', views.congregacao_cadastro, name="congregacao_cadastro"),
    url(r'^ cadastro_responsaveis/$', views.responsaveis, name="responsaveis"),
    url(r'^capitaes/$', views.capitaes, name="capitaes"),
    url(r'^passageiros/$', views.passageiros, name="passageiros"),
    url(r'^contato/$', views.contatos, name="contatos"),
    # Consultas
    url(r'^consulta_eventos/$', views.eventos_consulta, name="eventos_consulta"),
    url(r'^consulta_congregacao/$', views.congregacao_consulta, name="congregacao_consulta"),
    # Updates
    url(r'^eventos_update/(?P<pk>\d+)/$', views.eventos_update, name="eventos_update"),
    url(r'^congregacao_update/(?P<pk>\d+)/$', views.congregacao_update, name="congregacao_update"),
    # Deletes
    url(r'^eventos_delete/(?P<pk>\d+)/$', views.eventos_delete, name="eventos_delete"),
    url(r'^congregacao_delete/(?P<pk>\d+)/$', views.congregacao_delete, name="congregacao_delete"),
]
