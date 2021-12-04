from django.db import models

# Create your models here.

class Message(models.Model):
    time = models.DateTimeField(auto_now=True)
    sender = models.CharField(max_length=200, null=True, blank=True)
    reciever = models.CharField(max_length=200, null=True, blank=True)
    mesg = models.CharField(max_length=10000)
    is_read = models.BooleanField(default=False)

class Files(models.Model):
    created = models.DateTimeField(auto_now=True)
    file = models.FileField(verbose_name='FILE', upload_to='uploads%y%m%d')
    sender = models.CharField(max_length=200, blank=True)
    reciever = models.CharField(max_length=200, blank=True)
    on_proccess = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

class Sender(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200, blank=True)
    password = models.CharField(verbose_name='Password',max_length=200, blank=True)

    def __str__(self):
        return self.name

class Reciever(models.Model):
    name = models.CharField(verbose_name='Name',  max_length=200, blank=True)
    email = models.EmailField(verbose_name='Email', max_length=200, blank=True)

    def __str__(self):
        return self.name
