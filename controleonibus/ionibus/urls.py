from django.conf.urls import url, include

from controleonibus.ionibus import views

urlpatterns = [
    # Tela Principal
    url(r'^$', views.painel, name="painel"),
    # Telas de Cadastro
    url(r'^cadastro_eventos/$', views.eventos_cadastro, name="ionibus.add_eventos"),
    url(r'^cadastro_congregacao/$', views.congregacao_cadastro, name="ionibus.add_congregacao"),
    url(r'^cadastro_responsavel/$', views.responsavel_cadastro, name="ionibus.add_responsavel"),
    url(r'^cadastro_capitao/$', views.capitao_cadastro, name="ionibus.add_capitao"),
    url(r'^cadastro_passageiro/$', views.passageiro_cadastro, name="ionibus.add_passageiro"),    
    url(r'^lista_passageiro/$', views.listapassageiro_cadastro, name="ionibus.add_lista_passageiros"),    
    
    # Consultas
    url(r'^consulta_eventos/$', views.eventos_consulta, name="eventos_consulta"),
    url(r'^consulta_congregacao/$', views.congregacao_consulta, name="congregacao_consulta"),
    url(r'^consulta_responsavel/$', views.responsavel_consulta, name="responsavel_consulta"),    
    url(r'^consulta_capitao/$', views.capitao_consulta, name="capitao_consulta"),        
    url(r'^consulta_passageiro/$', views.passageiro_consulta, name="passageiro_consulta"),            
    # Updates
    url(r'^eventos_update/(?P<pk>\d+)/$', views.eventos_update, name="ionibus.change_eventos"),
    url(r'^congregacao_update/(?P<pk>\d+)/$', views.congregacao_update, name="ionibus.change_congregacao"),
    url(r'^responsavel_update/(?P<pk>\d+)/$', views.responsavel_update, name="ionibus.change_responsavel"),    
    url(r'^capitao_update/(?P<pk>\d+)/$', views.capitao_update, name="ionibus.change_capitao"),        
    url(r'^passageiro_update/(?P<pk>\d+)/$', views.passageiro_update, name="ionibus.change_passageiro"),            
    url(r'^listapassageiro_update/(?P<pk>\d+)/$', views.lista_passageiro_update, name="ionibus.change_lista_passageiros"),                
    # Deletes
    url(r'^eventos_delete/(?P<pk>\d+)/$', views.eventos_delete, name="ionibus.delete_eventos"),
    url(r'^congregacao_delete/(?P<pk>\d+)/$', views.congregacao_delete, name="ionibus.delete_congregacao"),
    url(r'^responsavel_delete/(?P<pk>\d+)/$', views.responsavel_delete, name="ionibus.delete_responsavel"),
    url(r'^capitao_delete/(?P<pk>\d+)/$', views.capitao_delete, name="ionibus.delete_capitao"),    
    url(r'^passageiro_delete/(?P<pk>\d+)/$', views.passageiro_delete, name="ionibus.delete_passageiro"),        
    # Página de Sem Permissão
    url(r'^sem_permissao/$', views.sempermissao, name="sempermissao"),
    # Relatórios
    url(r'^relatorio_eventos/$', views.eventos_relatorio, name="eventos_relatorio"),
    url(r'^relatorio_congregacao/$', views.congregacao_relatorio, name="congregacao_relatorio"),
    url(r'^relatorio_responsavel/$', views.responsavel_relatorio, name="responsavel_relatorio"),    
    # url(r'^relatorio_capitao/$', views.capitao_relatorio, name="capitao_relatorio"),        
    # url(r'^relatorio_passageiro/$', views.passageiro_relatorio, name="passageiro_relatorio"),            
]
