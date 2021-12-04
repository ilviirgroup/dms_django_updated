from rest_framework import serializers
from FILES.models import *

class MsgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'id', 'time', 'sender', 'reciever', 'mesg', 'is_read')

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Files
        fields = ('url', 'id', 'created', 'file', 'sender', 'reciever', 'on_proccess', 'completed')

class SenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sender
        fields = ('url', 'id', 'name', 'password')

class RecSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reciever
        fields = ('url', 'id', 'name', 'email')
