from django.contrib import admin
from FILES.models import Files, Reciever, Sender, Message

# Register your models here.
admin.site.register(Files)
admin.site.register(Sender)
admin.site.register(Reciever)
admin.site.register(Message)
