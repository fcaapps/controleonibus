from django.conf.urls import url, include

from controleonibus.ionibus import views


urlpatterns = [
    # Tela Principal
    url(r'^$', views.painel, name="painel"),
    # Telas de Cadastro
    url(r'^cadastro_eventos/$', views.eventos_cadastro, name="ionibus.add_eventos"),
    url(r'^cadastro_congregacao/$', views.congregacao_cadastro, name="congregacao_cadastro"),
    url(r'^ cadastro_responsaveis/$', views.responsaveis, name="responsaveis"),
    url(r'^capitaes/$', views.capitaes, name="capitaes"),
    url(r'^passageiros/$', views.passageiros, name="passageiros"),
    url(r'^contato/$', views.contatos, name="contatos"),
    # Consultas
    url(r'^consulta_eventos/$', views.eventos_consulta, name="eventos_consulta"),
    url(r'^consulta_congregacao/$', views.congregacao_consulta, name="congregacao_consulta"),
    # Updates
    url(r'^eventos_update/(?P<pk>\d+)/$', views.eventos_update, name="ionibus.change_eventos"),
    url(r'^congregacao_update/(?P<pk>\d+)/$', views.congregacao_update, name="congregacao_update"),
    # Deletes
    url(r'^eventos_delete/(?P<pk>\d+)/$', views.eventos_delete, name="ionibus.delete_eventos"),
    url(r'^congregacao_delete/(?P<pk>\d+)/$', views.congregacao_delete, name="congregacao_delete"),
    # Página de Sem Permissão
    url(r'^sem_permissao/$', views.sempermissao, name="sempermissao"),
    # Relatórios
    url(r'^relatorio_eventos/$', views.eventos_relatorio, name="eventos_relatorio"),
    url(r'^relatorio_congregacao/$', views.congregacao_relatorio, name="congregacao_relatorio"),
]
