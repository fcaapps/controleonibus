from django.shortcuts import render, redirect
from django.http import HttpResponse
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao
from controleonibus.ionibus.forms import EventosForm
from controleonibus.ionibus.forms import CongregacaoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# def home(request):
#     return render(request, 'home.html')

# Chama Tela Principal
@login_required
def painel(request):
    return render(request, 'painel.html')

# Chama Tela de Contatos
@login_required
def contatos(request):
    return render(request, 'contatos.html')

# Cadastro de Eventos
@login_required
def eventos_cadastro(request):
    form = EventosForm(request.POST or None)

    opcao = 'Eventos'

    context = {
        'form': form,
        'opcao': opcao,
    }

    if form.is_valid():
        form.save()
        return redirect('/consulta_eventos/')
    return render(request, 'cadastros.html', context)

# Altera Eventos
@login_required
def eventos_update(request,pk):
    evento = Eventos.objects.get(pk=pk)
    form = EventosForm(request.POST or None, instance=evento)

    opcao = 'Eventos'

    context = {
        'object': evento,
        'form': form,
        'opcao': opcao,
    }
    if form.is_valid():
        form.save()
        return redirect('/consulta_eventos/')
    return render(request, 'updates.html', context)

# Deleta Eventos
@login_required
def eventos_delete(request, pk):
    evento = Eventos.objects.get(pk=pk)

    opcao = 'Eventos'
    context = {
        'object': evento,
        'opcao': opcao,
    }

    if request.method=='POST':
        evento.delete()
        return redirect('/consulta_eventos/')
    return render(request, 'delete_confirm.html', context)

# Consulta Eventos com Paginador
@login_required
def eventos_consulta(request):
    evento_lista = Eventos.objects.all()
    paginator = Paginator(evento_lista, 100)  # Show 25 contacts per page

    opcao = 'Eventos'

    context = {
        'eventos': evento_lista,
        'opcao': opcao,
    }

    page = request.GET.get('page')
    try:
        eventos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        eventos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        eventos = paginator.page(paginator.num_pages)

    return render(request, 'consultas_de_cadastro.html', context)

# Cadastro de Congregação
@login_required
def congregacao_cadastro(request):
    form = CongregacaoForm(request.POST or None)

    opcao = 'Congregacao'

    context = {
        'form': form,
        'opcao': opcao,
    }

    if form.is_valid():
        form.save()
        return redirect('/consulta_congregacao/')
    return render(request, 'cadastros.html', context)

# Altera Congregação
@login_required
def congregacao_update(request,pk):
    congregacao = Congregacao.objects.get(pk=pk)
    form = CongregacaoForm(request.POST or None, instance=congregacao)

    opcao = 'Congregacao'

    context = {
        'object': congregacao,
        'form': form,
        'opcao': opcao,
    }
    if form.is_valid():
        form.save()
        return redirect('/consulta_congregacao/')
    return render(request, 'updates.html', context)

# Deleta Eventos
@login_required
def congregacao_delete(request, pk):
    congregacao = Congregacao.objects.get(pk=pk)

    opcao = 'Congregacao'
    context = {
        'object': congregacao,
        'opcao': opcao,
    }

    if request.method=='POST':
        congregacao.delete()
        return redirect('/consulta_congregacao/')
    return render(request, 'delete_confirm.html', context)

# Consulta Eventos com Paginador
@login_required
def congregacao_consulta(request):
    congregacao_lista = Congregacao.objects.all()
    paginator = Paginator(congregacao_lista, 100)  # Show 25 contacts per page

    opcao = 'Congregacao'

    context = {
        'congregacao': congregacao_lista,
        'opcao': opcao,
    }

    page = request.GET.get('page')
    try:
        congregacao = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        congregacao = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        congregacao = paginator.page(paginator.num_pages)

    return render(request, 'consultas_de_cadastro.html', context)


# Cadastro de Responsáveis
@login_required
def responsaveis(request):
    return render(request, 'responsaveis.html')

# Cadastro de Capitães
@login_required
def capitaes(request):
    return render(request, 'capitaes.html')

# Cadastro de Passageiros
@login_required
def passageiros(request):
    return render(request, 'passageiros.html')