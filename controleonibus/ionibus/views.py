from django.shortcuts import render, redirect
from django.http import HttpResponse
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao
from controleonibus.ionibus.models import Responsavel
from controleonibus.ionibus.models import Capitao
from controleonibus.ionibus.models import Passageiro
from controleonibus.ionibus.models import Lista_passageiros
from controleonibus.ionibus.forms import EventosForm
from controleonibus.ionibus.forms import CongregacaoForm
from controleonibus.ionibus.forms import ResponsavelForm
from controleonibus.ionibus.forms import CapitaoForm
from controleonibus.ionibus.forms import PassageiroForm
from controleonibus.ionibus.forms import ListaPassageiroForm
from controleonibus.tasks.serializers import EventosTaskSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table,TableStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
import reportlab 
from reportlab.lib.pagesizes import A4, cm
from django.views.generic import View
from reportlab.lib.colors import white, red, green, blue, gray, black
from datetime import date
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.generic.base import View
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import resolve

# Chama Tela Principal
@login_required
def painel(request):
    return render(request, 'painel.html')

# Chama Tela de Contatos
@login_required
def contatos(request):
    return render(request, 'contatos.html')

# Chama Tela Sem Permissão
@login_required
def sempermissao(request):
    return render(request, 'sempermissao.html')


# Cadastro de Eventos
@login_required
def eventos_cadastro(request):
    form = EventosForm(request.POST or None)
    urlName = resolve(request.path).url_name

    opcao = 'Eventos'

    context = {
        'form': form,
        'opcao': opcao,        
    }

    if "_min" in urlName:
        urlName = urlName[:-4]

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_eventos/')
        
    return render(request, 'cadastros.html', context)

# Altera Eventos
@login_required
def eventos_update(request,pk):
    evento = Eventos.objects.get(pk=pk)
    form = EventosForm(request.POST or None, instance=evento)
    urlName = resolve(request.path).url_name

    opcao = 'Eventos'

    context = {
        'object': evento,
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_eventos/')
    return render(request, 'updates.html', context)

# Deleta Eventos
@login_required
def eventos_delete(request, pk):
    evento = Eventos.objects.get(pk=pk)
    urlName = resolve(request.path).url_name

    opcao = 'Eventos'
    context = {
        'object': evento,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

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
    urlName = resolve(request.path).url_name

    opcao = 'Congregacao'

    context = {
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_congregacao/')
    return render(request, 'cadastros.html', context)

# Altera Congregação
@login_required
def congregacao_update(request,pk):
    congregacao = Congregacao.objects.get(pk=pk)
    form = CongregacaoForm(request.POST or None, instance=congregacao)
    urlName = resolve(request.path).url_name

    opcao = 'Congregacao'

    context = {
        'object': congregacao,
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_congregacao/')
    return render(request, 'updates.html', context)

# Deleta Congregação
@login_required
def congregacao_delete(request, pk):
    congregacao = Congregacao.objects.get(pk=pk)
    urlName = resolve(request.path).url_name

    opcao = 'Congregacao'
    context = {
        'object': congregacao,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if request.method=='POST':
        congregacao.delete()
        return redirect('/consulta_congregacao/')
    return render(request, 'delete_confirm.html', context)

# Consulta Congregação com Paginador
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
def responsavel_cadastro(request):
    form = ResponsavelForm(request.POST or None)
    urlName = resolve(request.path).url_name

    opcao = 'Responsavel'

    context = {
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_responsavel/')
    return render(request, 'cadastros.html', context)

# Altera Responsavel
@login_required
def responsavel_update(request,pk):
    responsavel = Responsavel.objects.get(pk=pk)
    form = ResponsavelForm(request.POST or None, instance=responsavel)
    urlName = resolve(request.path).url_name

    opcao = 'Responsavel'

    context = {
        'object': responsavel,
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_responsavel/')
    return render(request, 'updates.html', context)

# Deleta Responsavel
@login_required
def responsavel_delete(request, pk):
    responsavel = Responsavel.objects.get(pk=pk)
    urlName = resolve(request.path).url_name

    opcao = 'Responsavel'

    context = {
        'object': responsavel,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if request.method=='POST':
        responsavel.delete()
        return redirect('/consulta_responsavel/')
    return render(request, 'delete_confirm.html', context)

# Consulta Responsavel com Paginador
@login_required
def responsavel_consulta(request):
    responsavel_lista = Responsavel.objects.all()
    paginator = Paginator(responsavel_lista, 100)  # Show 25 contacts per page

    opcao = 'Responsavel'

    context = {
        'responsavel': responsavel_lista,
        'opcao': opcao,
    }

    page = request.GET.get('page')
    try:
        responsavel = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        responsavel = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        responsavel = paginator.page(paginator.num_pages)

    return render(request, 'consultas_de_cadastro.html', context)
    

# Cadastro de Capitães
@login_required
def capitao_cadastro(request):
    form = CapitaoForm(request.POST or None)
    urlName = resolve(request.path).url_name

    opcao = 'Capitao'

    context = {
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_capitao/')
    return render(request, 'cadastros.html', context)

# Altera Capitão
@login_required
def capitao_update(request,pk):
    capitao = Capitao.objects.get(pk=pk)
    form = CapitaoForm(request.POST or None, instance=capitao)
    urlName = resolve(request.path).url_name

    opcao = 'Capitao'

    context = {
        'object': capitao,
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_capitao/')
    return render(request, 'updates.html', context)

# Deleta Capitão
@login_required
def capitao_delete(request, pk):
    capitao = Capitao.objects.get(pk=pk)
    urlName = resolve(request.path).url_name

    opcao = 'Capitao'

    context = {
        'object': capitao,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if request.method=='POST':
        capitao.delete()
        return redirect('/consulta_capitao/')
    return render(request, 'delete_confirm.html', context)

# Consulta Capitão com Paginador
@login_required
def capitao_consulta(request):
    capitao_lista = Capitao.objects.all()
    paginator = Paginator(capitao_lista, 100)  # Show 25 contacts per page

    opcao = 'Capitao'

    context = {
        'capitao': capitao_lista,
        'opcao': opcao,
    }

    page = request.GET.get('page')
    try:
        capitao = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        capitao = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        capitao = paginator.page(paginator.num_pages)

    return render(request, 'consultas_de_cadastro.html', context)

# Cadastro de Passageiros
@login_required
def passageiro_cadastro(request):
    form = PassageiroForm(request.POST or None)
    urlName = resolve(request.path).url_name

    opcao = 'Passageiro'

    context = {
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_passageiro/')
    return render(request, 'cadastros.html', context)

# Altera Passageiros
@login_required
def passageiro_update(request,pk):
    passageiro = Passageiro.objects.get(pk=pk)
    form = PassageiroForm(request.POST or None, instance=passageiro)
    urlName = resolve(request.path).url_name

    opcao = 'Passageiro'

    context = {
        'object': passageiro,
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()
        return redirect('/consulta_passageiro/')
    return render(request, 'updates.html', context)

# Deleta Passageiros
@login_required
def passageiro_delete(request, pk):
    passageiro = Passageiro.objects.get(pk=pk)
    urlName = resolve(request.path).url_name

    opcao = 'Passageiro'

    context = {
        'object': passageiro,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if request.method=='POST':
        passageiro.delete()
        return redirect('/consulta_passageiro/')
    return render(request, 'delete_confirm.html', context)

# Consulta Passageiro com Paginador
@login_required
def passageiro_consulta(request):
    passageiro_lista = Passageiro.objects.all()
    paginator = Paginator(passageiro_lista, 100)  # Show 25 contacts per page

    opcao = 'Passageiro'

    context = {
        'passageiro': passageiro_lista,
        'opcao': opcao,
    }

    page = request.GET.get('page')
    try:
        passageiro = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        passageiro = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        passageiro = paginator.page(paginator.num_pages)

    return render(request, 'consultas_de_cadastro.html', context)


# Cadastro de Lista de Passageiros
@login_required
def listapassageiro_cadastro(request):
    form = ListaPassageiroForm(request.POST or None)
    lista_passageiro = Lista_passageiros.objects.all()

    urlName = resolve(request.path).url_name

    opcao = 'ListaPassageiro'

    context = {
        'lista_passageiro': lista_passageiro,    
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()

    return render(request, 'cadastros.html', context)

# Altera Lista de Passageiros
@login_required
def lista_passageiro_update(request,pk):
    lista_passageiro = Lista_passageiros.objects.get(pk=pk)
    form = ListaPassageiroForm(request.POST or None, instance=Lista_passageiros)
    urlName = resolve(request.path).url_name

    opcao = 'lista_passageiro'

    context = {
        'object': Lista_passageiros,
        'form': form,
        'opcao': opcao,
    }

    if not request.user.has_perm(urlName):
        return redirect('/sem_permissao/')

    if form.is_valid():
        form.save()

    return render(request, 'cadastros.html', context)

# # Deleta Passageiros
# @login_required
# def passageiro_delete(request, pk):
#     passageiro = Passageiro.objects.get(pk=pk)
#     urlName = resolve(request.path).url_name

#     opcao = 'Passageiro'

#     context = {
#         'object': passageiro,
#         'opcao': opcao,
#     }

#     if not request.user.has_perm(urlName):
#         return redirect('/sem_permissao/')

#     if request.method=='POST':
#         passageiro.delete()
#         return redirect('/consulta_passageiro/')
#     return render(request, 'delete_confirm.html', context)

# # Consulta Passageiro com Paginador
# @login_required
# def passageiro_consulta(request):
#     passageiro_lista = Passageiro.objects.all()
#     paginator = Paginator(passageiro_lista, 100)  # Show 25 contacts per page

#     opcao = 'Passageiro'

#     context = {
#         'passageiro': passageiro_lista,
#         'opcao': opcao,
#     }

#     page = request.GET.get('page')
#     try:
#         passageiro = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         passageiro = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         passageiro = paginator.page(paginator.num_pages)

#     return render(request, 'consultas_de_cadastro.html', context)


#
# R E L A T Ó R I O S 
#

# Imprimir Relatório de Eventos
@login_required
def eventos_relatorio(request):
    eventos = Eventos.objects.all()

    response = HttpResponse(content_type='application/pdf')
 
    # Criar o PDF Objeto
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Titulo
    PAGE_HEIGHT=defaultPageSize[1]  
    PAGE_WIDTH=defaultPageSize[0]  

    c.setTitle("Relação de Eventos")

    c.setFont('Helvetica', 25)
    c.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-53, "Relação de Eventos")

    # Cabeçalho
    c.setLineWidth(.3)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(55,800,'iOnibus')
    
    c.setFont('Helvetica', 10)
    c.drawString(30,785,'Sistema de Controle')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(502,800,'Impresso em:')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(515,785,date.today().strftime("%d-%m-%Y"))
    
    c.line(30,770,567,770)

    # Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontsize = 10
    styleBH.color = red

    # Titulo da Tabela
    tipo = Paragraph('''Tipo''',styleBH)
    circuito = Paragraph('''Circuito''',styleBH)
    # parte = Paragraph('''Parte''',styleBH)
    datadoevento = Paragraph('''Data do Evento''',styleBH)    
    textobase = Paragraph('''Texto Base''',styleBH)

    data = []

    data.append([tipo,circuito,datadoevento,textobase])

    # styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7


    # Table Details
    high = 730
    for evento in eventos:
        vtipo = ''
        if evento.tipo == 'AC':
            vtipo = 'Assembléia de Circuito'
        elif evento.tipo == 'AE':            
            vtipo = 'Assembléia de Especial'
        elif evento.tipo == 'CR':            
            vtipo = 'Congresso Regional'

        dataevento = evento.data_evento.strftime("%d-%m-%Y")            

        this_evento = [vtipo, evento.circuito, dataevento, evento.texto_base]        
        data.append(this_evento)        
        high = high - 18

    # Table Size
    width, height = A4
    table = Table(data,colWidths=[6.7 * cm, 5.2 * cm, 3.0 * cm, 4.0 * cm])    
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black), ]))
        
    # Pdf Size
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    c.showPage()    
    
    # Salva PDF
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


# Imprimir Relatório de Congregações
@login_required
def congregacao_relatorio(request):
    congregacoes = Congregacao.objects.all()

    response = HttpResponse(content_type='application/pdf')
 
    # Criar o PDF Objeto
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Titulo
    PAGE_HEIGHT=defaultPageSize[1]  
    PAGE_WIDTH=defaultPageSize[0]  

    c.setTitle("Relação de Congregações")

    c.setFont('Helvetica', 25)
    c.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-53, "Relação de Congregações")

    # Cabeçalho
    c.setLineWidth(.3)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(55,800,'iOnibus')
    
    c.setFont('Helvetica', 10)
    c.drawString(30,785,'Sistema de Controle')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(502,800,'Impresso em:')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(515,785,date.today().strftime("%d-%m-%Y"))
    
    c.line(30,770,567,770)

    # Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontsize = 10
    styleBH.color = red

    # Titulo da Tabela
    nomecongregacao = Paragraph('''Congregação''',styleBH)
    coordenador = Paragraph('''Coordenador''',styleBH)
    telcoordenador = Paragraph('''Tel. Coordenador''',styleBH)
    emailcoordenador = Paragraph('''E-mail do Coordenador''',styleBH)    

    data = []

    data.append([nomecongregacao, coordenador,telcoordenador,emailcoordenador])

    # styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7


    # Table Details
    high = 730
    for congregacao in congregacoes:        
        this_congregacao = [congregacao.nome, congregacao.coordenador, congregacao.tel_coordenador,congregacao.email_coordenador]        
        data.append(this_congregacao)        
        high = high - 18

    # Table Size
    width, height = A4
    table = Table(data,colWidths=[4.5 * cm, 4.0 * cm, 3.5 * cm, 6.92 * cm])    
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black), ]))
        
    # Pdf Size
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    c.showPage()    
    
    # Salva PDF
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

    

# Imprimir Relatório de Responsavel
@login_required
def responsavel_relatorio(request):
    responsaveis = Responsavel.objects.all()

    response = HttpResponse(content_type='application/pdf')
 
    # Criar o PDF Objeto
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Titulo
    PAGE_HEIGHT=defaultPageSize[1]  
    PAGE_WIDTH=defaultPageSize[0]  

    c.setTitle("Relação de Responsáveis")

    c.setFont('Helvetica', 25)
    c.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-53, "Relação de Responsáveis")

    # Cabeçalho
    c.setLineWidth(.3)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(55,800,'iOnibus')
    
    c.setFont('Helvetica', 10)
    c.drawString(30,785,'Sistema de Controle')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(502,800,'Impresso em:')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(515,785,date.today().strftime("%d-%m-%Y"))
    
    c.line(30,770,567,770)

    # Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontsize = 10
    styleBH.color = red

    # Titulo da Tabela
    nomeresponsavel = Paragraph('''Responsável''',styleBH)
    tipo = Paragraph('''Tipo''',styleBH)
    congregacao = Paragraph('''Congregação''',styleBH)
    telefone = Paragraph('''Telefone''',styleBH)    

    data = []

    data.append([nomeresponsavel, tipo, congregacao, telefone])

    # styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7


    # Table Details
    high = 730
    for responsa in responsaveis:        
        vtipo = ''
        if responsa.tipo == 'EG':
            vtipo ='Enc. Geral'
        elif responsa.tipo == 'EC':            
            vtipo = 'Enc. de Congregação'
        elif responsa.tipo == 'EE':            
            vtipo = 'Enc. do Evento'
        elif responsa.tipo == 'AC':            
            vtipo = 'Aj. de Congregação'
        elif responsa.tipo == 'AE':            
            vtipo = 'Aj. do Evento'

        this_responsavel = [responsa.nome, vtipo, responsa.congregacao, responsa.telefone]        
        data.append(this_responsavel)        
        high = high - 18

    # Table Size
    width, height = A4
    table = Table(data,colWidths=[8.1 * cm, 3.8 * cm, 4.0 * cm, 3.0 * cm])    
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black), ]))
        
    # Pdf Size
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    c.showPage()    
    
    # Salva PDF
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response



# # Imprimir Relatório de Capitão
# @login_required
# def capitao_relatorio(request):
#     congregacao = Congregacao.objects.all()
#     capitaes = Capitao.objects.all()

#     response = HttpResponse(content_type='application/pdf')
 
#     # Criar o PDF Objeto
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer, pagesize=A4)

#     #Titulo
#     PAGE_HEIGHT=defaultPageSize[1]  
#     PAGE_WIDTH=defaultPageSize[0]  

#     c.setTitle("Relação de Capitães")

#     c.setFont('Helvetica', 25)
#     c.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-53, "Relação de Capitães")

#     # Cabeçalho
#     c.setLineWidth(.3)
#     c.setFont('Helvetica-Bold', 12)
#     c.drawString(55,800,'iOnibus')
    
#     c.setFont('Helvetica', 10)
#     c.drawString(30,785,'Sistema de Controle')

#     c.setFont('Helvetica-Bold', 10)
#     c.drawString(502,800,'Impresso em:')

#     c.setFont('Helvetica-Bold', 10)
#     c.drawString(515,785,date.today().strftime("%d-%m-%Y"))
    
#     c.line(30,770,567,770)

#     # Table header
#     styles = getSampleStyleSheet()
#     styleBH = styles["Normal"]
#     styleBH.alignment = TA_CENTER
#     styleBH.fontsize = 10
#     styleBH.color = red

#     # Titulo da Tabela
#     nomeresponsavel = Paragraph('''Responsável''',styleBH)
#     tipo = Paragraph('''Tipo''',styleBH)
#     congregacao = Paragraph('''Congregação''',styleBH)
#     telefone = Paragraph('''Telefone''',styleBH)    

#     data = []

#     data.append([nomeresponsavel, tipo, congregacao, telefone])

#     # styles = getSampleStyleSheet()
#     styleN = styles["BodyText"]
#     styleN.alignment = TA_CENTER
#     styleN.fontSize = 7


#     # Table Details
#     high = 730
#     for responsa in responsaveis:        
#         vtipo = ''
#         if responsa.tipo == 'EG':
#             vtipo ='Enc. Geral'
#         elif responsa.tipo == 'EC':            
#             vtipo = 'Enc. de Congregação'
#         elif responsa.tipo == 'EE':            
#             vtipo = 'Enc. do Evento'
#         elif responsa.tipo == 'AC':            
#             vtipo = 'Aj. de Congregação'
#         elif responsa.tipo == 'AE':            
#             vtipo = 'Aj. do Evento'

#         this_responsavel = [responsa.nome, vtipo, responsa.congregacao, responsa.telefone]        
#         data.append(this_responsavel)        
#         high = high - 18

#     # Table Size
#     width, height = A4
#     table = Table(data,colWidths=[8.1 * cm, 3.8 * cm, 4.0 * cm, 3.0 * cm])    
#     table.setStyle(TableStyle([
#         ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
#         ('BOX', (0,0), (-1,-1), 0.25, colors.black), ]))
        
#     # Pdf Size
#     table.wrapOn(c, width, height)
#     table.drawOn(c, 30, high)
#     c.showPage()    
    
#     # Salva PDF
#     c.save()
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response
