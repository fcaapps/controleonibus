from django.forms import ModelForm
from controleonibus.ionibus.models import Eventos
from controleonibus.ionibus.models import Congregacao

class EventosForm(ModelForm):
    class Meta:
        model = Eventos
        exclude = ['id', 'criado_em', 'atualizado_em']

class CongregacaoForm(ModelForm):
    class Meta:
        model = Congregacao
        exclude = ['id', 'criado_em', 'atualizado_em']