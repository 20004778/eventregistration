from django.db import models
from django.contrib import admin
# Create your models here.
class participant(models.Model):
    name = models.CharField(max_length=100)
    insitution = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    
    
class participantAdmin(admin.ModelAdmin):
    list_display = ('name', 'insitution', 'email','phone')

