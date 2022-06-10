
from datetime import date
from pyexpat import model
from tkinter.tix import Select
from django.db import models


# Create your models here.
#makemigrations= create changes and store it in file_
#migrate= apply pending changes created by makemigrations

class Contact(models.Model):
    name =models.CharField(max_length=20,default=20 )
    email =models.CharField(max_length=202,default=20)
    phone =models.CharField(max_length=20,default=20)
    desc =models.TextField(max_length=200,default=20)
    date =models.DateField()

class services(models.Model):
 Select = models.CharField(max_length=250)
 name =models.CharField(max_length=20,default=20 )
