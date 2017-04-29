from django.conf.urls import url, include

from controleonibus.accounts.views import register

from django.contrib.auth.views import login

from django.contrib.auth.views import logout

urlpatterns = [
    # Contas
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'},  name="login"),
    url(r'^sair/$', logout, {'next_page': 'accounts:login'}, name="logout"),
    url(r'^registre-se/$', register, name="register"),
]

