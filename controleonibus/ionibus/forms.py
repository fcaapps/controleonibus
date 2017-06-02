from django.forms import ModelForm
from django import forms
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao
from controleonibus.ionibus.models import Responsavel
from controleonibus.ionibus.models import Capitao
from controleonibus.ionibus.models import Passageiro
from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateWidget

class EventosForm(ModelForm):
    class Meta:
        model = Eventos
        exclude = ['id', 'criado_em', 'atualizado_em']
        # widgets = { 
        #    # 'data_evento': DatePicker(options={"format":"DD-MM-YYYY", "id":"id_data_evento", "pickTime": "True"}),
        #    'data_evento': DateWidget(attrs={'id':"id_data_evento"}, usel10n = True, bootstrap_version=3)
        # }

class CongregacaoForm(ModelForm):
    class Meta:
        model = Congregacao
        exclude = ['id', 'criado_em', 'atualizado_em']

class ResponsavelForm(ModelForm):
    class Meta:
        model = Responsavel
        exclude = ['id', 'criado_em', 'atualizado_em']        

class CapitaoForm(ModelForm):
    class Meta:
        model = Capitao
        exclude = ['id', 'criado_em', 'atualizado_em']                

class PassageiroForm(ModelForm):
    class Meta:
        model = Passageiro
        exclude = ['id', 'criado_em', 'atualizado_em']                        