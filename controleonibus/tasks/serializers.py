from rest_framework import serializers
from controleonibus.ionibus.models import Eventos

from django.contrib.auth.models import User

class EventosTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = ['id', 'tipo', 'data_evento', 'circuito', 'parte', 'texto_base', 'owner']

class UserSerializer(serializers.ModelSerializer):
	tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Eventos.objects.all())
	
	class Meta:
		model = User
		fields = ('id','username','tasks')
