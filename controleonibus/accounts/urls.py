from django.conf.urls import url, include

from controleonibus.accounts.views import register

from controleonibus.accounts import views

from django.contrib.auth.views import login

from django.contrib.auth.views import logout

urlpatterns = [
    # Contas
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'},  name="login"),
    url(r'^sair/$', logout, {'next_page': 'accounts:login'}, name="logout"),
    url(r'^registre-se/$', register, name="register"),
    url(r'^editar-senha/$', views.edit_password, name="edit_password"),
    url(r'^aviso-senha-alterada/$', views.aviso_senha_alterada, name="senha_alterada"),
]

