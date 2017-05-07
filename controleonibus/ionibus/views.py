from django.shortcuts import render, redirect
from django.http import HttpResponse
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao
from controleonibus.ionibus.forms import EventosForm
from controleonibus.ionibus.forms import CongregacaoForm
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
    parte = Paragraph('''Parte''',styleBH)
    datadoevento = Paragraph('''Data do Evento''',styleBH)    
    textobase = Paragraph('''Texto Base''',styleBH)

    data = []

    data.append([tipo,circuito,parte,datadoevento,textobase])

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

        this_evento = [vtipo, evento.circuito, evento.parte, dataevento, evento.texto_base]        
        data.append(this_evento)        
        high = high - 18

    # Table Size
    width, height = A4
    table = Table(data,colWidths=[8.7 * cm, 1.7 * cm, 1.5 * cm, 3.0 * cm, 4.0 * cm])    
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

    