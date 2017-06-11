from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import datetime

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Circuito(models.Model):

    PARTE = (
        ('A', 'A'),
        ('B', 'B'),
    )

    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=4)
    parte = models.CharField('Parte', max_length=1, choices=PARTE)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True, null=True, blank=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True, null=True, blank=True)
    usuario = models.ForeignKey('auth.User', related_name='tasks', null=True, blank=True)

    class Meta: 
        verbose_name_plural = 'Circuito'         

    def __str__(self):
        return self.sigla + ' - ' + self.nome

class Eventos(models.Model):
    TIPO_EVENTO = (
        ('AC', 'Assembléia de Circuito'),
        ('AE', 'Assembléia Especial'),
        ('CR', 'Congresso Regional'),
    )

    LOCAL_EVENTO = (
        ('01', 'Salão de Assembléias'),
        ('02', 'Ginásio Paulo Sarasate'),
        ('03', 'Estádio Castelão'),
    )

    STATUS_EVENTO = (
        ('01', 'Aberto'),
        ('02', 'Encerrado')
    )


    # CIRCUITO = (
    #     ('CE01', 'CE01'),
    #     ('CE02', 'CE02'),
    #     ('CE03', 'CE03'),
    #     ('CE04', 'CE04'),
    #     ('CE05', 'CE05'),
    #     ('CE06', 'CE06'),
    #     ('CE07', 'CE07'),
    #     ('CE08', 'CE08'),
    #     ('CE09', 'CE09'),
    #     ('CE10', 'CE10'),
    #     ('CE11', 'CE11'),
    #     ('CE12', 'CE12'),
    #     ('CE13', 'CE13'),
    #     ('CE14', 'CE14'),
    #     ('CE15', 'CE15'),
    #     ('CE16', 'CE16'),
    #     ('CE17', 'CE17'),
    #     ('CE18', 'CE18'),
    # )

    # PARTE = (
    #     ('A', 'A'),
    #     ('B', 'B'),
    # )


    tipo = models.CharField('Tipo', max_length=2, choices=TIPO_EVENTO)
    data_evento = models.DateTimeField(
        'Data do Evento', null=True, blank=True
    )
    # circuito = models.CharField('Circuito', max_length=4, choices=CIRCUITO, blank=True)
    circuito = models.ForeignKey('ionibus.circuito', related_name='fk_CircuitoEven', null=True, blank=True)
    # parte = models.CharField('Parte', max_length=1, choices=PARTE, blank=True)
    texto_base = models.CharField('Texto Base', max_length=30, blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    local = models.CharField('Local do Evento', max_length=50, choices=LOCAL_EVENTO, blank=True, default='01')
    status_evento = models.CharField('Status do Evento', max_length=50, choices=STATUS_EVENTO, blank=True, default='01')

    class Meta: 
        verbose_name_plural = 'Eventos'          

    def __str__(self):


        if self.tipo == 'AC':
            return 'Tipo: Assemb. de Circuito' + ' - Data do Evento: ' + str(self.data_evento.strftime('%d/%m/%Y'))
        if self.tipo == 'AE':
            return 'Tipo: Assemb. Especial' + ' - Data do Evento: ' + str(self.data_evento.strftime('%d/%m/%Y'))
        if self.tipo == 'CR':
            return 'Tipo: Cong. Regional' + ' - Data do Evento:' + str(self.data_evento.strftime('%d/%m/%Y'))


class Congregacao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=200, null=True, blank=True)
    coordenador = models.CharField('Coordenador', max_length=50)
    tel_coordenador = models.CharField('Telefone Coordenador', max_length=30)
    email_coordenador = models.CharField('E-mail', max_length=100)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    circuito = models.ForeignKey('ionibus.circuito', related_name='fk_CircuitoCong', null=True, blank=True)

    class Meta: 
        verbose_name_plural = 'Congregação'          

    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    ENCARREGADO = (
        ('EG', 'Encarregado Geral'),                
        ('EC', 'Encarregado de Congregação'),
        ('EE', 'Encarregado do Evento'),
        ('AC', 'Ajudante de Congregação'),
        ('AE', 'Ajudante do Evento'),
    )

    nome = models.CharField('Nome', max_length=100)
    tipo = models.CharField('Tipo', max_length=2, choices=ENCARREGADO) # {EC = ENCARREGADO DA CONGREGAÇÃO, EE = ENCARREGADO DO EVENTO, AC - AJUDANTE DA CONGREGAÇÃO, AE - AJUDANTE DO EVENTO}
    congregacao = models.ForeignKey('ionibus.congregacao', related_name='fk_cong_Responsavel', null=True, blank=True)
    email = models.CharField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=30)
    foto = models.ImageField(
        upload_to='ionibus/images', verbose_name='Imagem', null=True, blank=True
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta: 
        verbose_name_plural = 'Responsável'          

    def __str__(self):
        return self.nome
    

class Capitao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    congregacao = models.ForeignKey('ionibus.congregacao', related_name='fk_cong_Capitao', null=True, blank=True)
    responsavel = models.ForeignKey('ionibus.responsavel', related_name='fk_resp_Capitao', null=True, blank=True)
    telefone1 = models.CharField('Telefone 1', max_length=30)
    telefone2 = models.CharField('Telefone 2', max_length=30, null=True, blank=True)
    foto = models.ImageField(
        upload_to='ionibus/images', verbose_name='Imagem', null=True, blank=True
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta: 
        verbose_name_plural = 'Capitão'          

    def __str__(self):
        return self.nome

class Passageiro(models.Model):
    CRIANCA_COLO = (
        ('S', 'Sim'),                
        ('N', 'Não'),
    )

    nome = models.CharField('Nome', max_length=100)
    congregacao = models.ForeignKey('ionibus.congregacao', related_name='fk_cong_Passageiro', null=True, blank=True)
    rg_cpf = models.CharField('RG/CPF', max_length=30)
    capitao = models.ForeignKey('ionibus.capitao', related_name='fk_cap_Passageiro', null=True, blank=True)
    crianca_colo = models.CharField('Criança de Colo', max_length=1, default='N', choices=CRIANCA_COLO)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
   
    class Meta: 
        verbose_name_plural = 'Passageiro'          

    def __str__(self):
        return self.nome + ' - ' + self.rg_cpf


class Onibus_assentos(models.Model):    
    evento = models.ForeignKey('ionibus.eventos', related_name='fk_eve_onibus_assentos', null=True, blank=True)
    congregacao = models.ForeignKey('ionibus.congregacao', related_name='fk_cong_onibus_assentos', null=True, blank=True)
    qt_onibus = models.IntegerField('Qt. Ônibus')
    qt_assentos = models.IntegerField('Qt. Assentos')
    valor_passagem = models.DecimalField('Qt. Assentos', max_digits=10, decimal_places=2)
    
    class Meta: 
        verbose_name_plural = 'Ônibus Assentos'          

    def __str__(self):
        return self.evento + ' - ' + self.congregacao + ' - Qt.O: ' + self.qt_onibus + ' - Qt.A: ' + self.qt_assentos

class Lista_passageiros(models.Model):    
    PAGO = (
        ('S', 'Sim'),                
        ('N', 'Não'),
    )

    data_arranjo = models.DateField(
        'Data do Arranjo', null=True, blank=True
    )
    evento = models.ForeignKey('ionibus.eventos', related_name='fk_eve_lista_passageiros', null=True, blank=True)
    congregacao = models.ForeignKey('ionibus.congregacao', related_name='fk_cong_lista_passageiros')
    endereco_primeira_parada = models.CharField('Primeira parada', max_length=200)
    endereco_segunda_parada = models.CharField('Segunda parada', max_length=200)
    endereco_terceira_parada = models.CharField('Terceira parada', max_length=200)
    capitao = models.ForeignKey('ionibus.capitao', related_name='fk_cap_lista_passageiros')    
    onibus = models.ForeignKey('ionibus.onibus_assentos', related_name='fk_onibus_a_lista_passageiros', null=True, blank=True)    
    passageiro = models.ForeignKey('ionibus.passageiro', related_name='fk_passa_lista_passageiros')    
    pago = models.CharField('Pago', max_length=1, default='N', choices=PAGO)        

    class Meta: 
        verbose_name_plural = 'Lista de Passageiros'          

    def __str__(self):
        return self.congregacao + ' - ' + self.data_arranjo.strftime('%d/%m/%Y') + ' - ' + self.passageiro

class Pagamentos(models.Model):
    lista = models.ForeignKey('ionibus.lista_passageiros', related_name='fk_lista_pagamentos')    
    data_pgto = models.DateField(
        'Data do Pagto', null=True, blank=True
    )
    valor_pago = models.DecimalField('Qt. Pago', max_digits=10, decimal_places=2)

