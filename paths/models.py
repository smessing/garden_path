from django.db import models

class Path(models.Model):
"""A new garden path through wikipedia.

Fields:
auth_email -- author's e-mail
auth_name -- author's name
nick -- a short nickname for url purposes
pub_date -- date published
title -- title of the garden path

"""
  auth_email = models.EmailField()
  auth_name = models.CharField(max_length=200)
  nick = models.SlugField()
  pub_date = models.DateTimeField('date published')
  title = models.CharField(max_length=300) 

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'paths'
    ordering = ['pub_date']

class Blob(models.Model):
"""One step in a garden path.

Fields:
body -- text of the blob
article -- url to wikipedia origin
parent -- the garden path this blog comes from
position -- position in the garden path

""" 

  body = models.TextField()
  article = models.URLField()
  parent = models.ForeignKey(Path)
  position = models.IntegerField()
