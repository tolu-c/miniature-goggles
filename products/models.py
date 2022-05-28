from turtle import title
from django.db import models

# Create your models here.
class Category(models.Model):
  title= models.charField(max_length=255)