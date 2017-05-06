from django.shortcuts import render, redirect
from django.http import HttpResponse
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao
from controleonibus.ionibus.forms import EventosForm
from controleonibus.ionibus.forms import CongregacaoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table,TableStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.enums import TA_CENTER
import reportlab 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.views.generic import View
from controleonibus.ionibus.utils import render_to_pdf #created in step 4

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

# Imprimir relatório
@login_required
def eventos_relatorio(request):
    eventos = Eventos.objects.all()
    # context = {
    #     'eventos': evento_lista,        
    # }

    # Criar o HttpResponse Cabeçalho with PDF
    pdf = render_to_pdf('reports/report_eventos.html')
    response = HttpResponse(pdf,content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=relatorio.pdf'

    # Criar o PDF Objeto
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    # Cabeçalho
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'FCA')
    
    c.setFont('Helvetica', 12)
    c.drawString(30,735,'Relatório')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750,'01/07/2016')
    
    c.line(460,747,560,747)

    # Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontsize = 10

    tipo = Paragraph('''Tipo''',styleBH)
    circuito = Paragraph('''Circuito''',styleBH)
    parte = Paragraph('''Parte''',styleBH)
    # datadoevento = Paragraph('''Data do Evento''',styleBH)    
    textobase = Paragraph('''Texto Base''',styleBH)

    data = []

    data = [[tipo,circuito,parte,textobase]]

    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontsize = 7

    # Table Details
    high = 650
    for evento in eventos:
        # this_evento = [evento['tipo'], evento['circuito'], evento['parte'], evento['data_evento'], evento['texto_base']]
        data = [evento.tipo, evento.circuito, evento.parte, evento.texto_base]        
        # data.append(this_evento)
        high = high - 18

    # Table Size
    width, height = A4
    table = Table(data,colWidths=[9.5 * cm, 1.9 * cm, 1.9 * cm, 1.9 * cm])    
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

# Testando xhtml2pdf 
def eventos_report(request, *args, **kwargs):
    evento_lista = Eventos.objects.all()
    context = {
        'eventos': evento_lista,        
    }
        # pdf = render_to_pdf('pdf/invoice.html', data)
        # return HttpResponse(pdf, content_type='application/pdf')
    pdf = render_to_pdf('reports/report_eventos.html', context)
    return HttpResponse(pdf, content_type='application/pdf')