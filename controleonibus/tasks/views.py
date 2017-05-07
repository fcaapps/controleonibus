from django.shortcuts import render
from controleonibus.ionibus.models import Eventos
from rest_framework import viewsets
from controleonibus.tasks.serializers import EventosTaskSerializer, UserSerializer
from django.contrib.auth.models import User

class EventosTaskViewSet(viewsets.ModelViewSet):
	queryset = Eventos.objects.all().order_by('-criado_em')
	serializer_class = EventosTaskSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer	