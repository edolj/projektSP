from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class Article(models.Model):
  title = models.CharField(max_length=100, default='')
  content = models.TextField()
  pub_date = models.DateTimeField( default=datetime.now )
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  
"""
podatki za napravo
"""  
class Naprava(models.Model):
  imeNaprave = models.CharField(max_length=60, default='')
  opis = models.TextField()
  cena = models.IntegerField()
  picture = models.FileField()
  video = models.FileField()
  pub_date = models.DateTimeField( default=datetime.now )
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  """
  return True if object's price is larger then suggested, otherwise False
  """
  def is_expensive(self):
    if self.cena >= 1500:
      return True
  
    return False
  
  """
  adding permissions for users
  """
  class Meta:
    permissions = (
      ('edit_naprava', 'Can edit naprava'),
    )  
  
class Comment(models.Model):
  comment = models.TextField()
  pub_date = models.DateTimeField( default=datetime.now )
  naprava = models.ForeignKey(Naprava, on_delete=models.CASCADE, null=True )
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  