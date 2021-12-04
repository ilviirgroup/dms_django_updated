from rest_framework import viewsets
from rest_framework import filters
from FILES.serializers import*
from FILES.models import *
# Create your views here.

class MsgCreate(viewsets.ModelViewSet):
    search_fields = ['id', 'mesg', 'is_read', 'time', 'sender', 'reciever']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MsgSerializer
    queryset = Message.objects.all().order_by('-id')

class FileCreate(viewsets.ModelViewSet):
    search_fields = ['id', 'on_proccess', 'completed']
    filter_backends = (filters.SearchFilter,)
    serializer_class = FileSerializer
    queryset = Files.objects.all().order_by('-id')

class SenCreate(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SenSerializer
    queryset = Sender.objects.all().order_by('-id')

class RecCreate(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = RecSerializer
    queryset = Reciever.objects.all().order_by('-id')