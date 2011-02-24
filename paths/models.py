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
  auth_fname = models.CharField(max_length=200)
  auth_lname = models.CharField(max_length=200)
  nick = models.SlugField()
  pub_date = models.DateTimeField('date published')
  title = models.CharField(max_length=300) 

  def _get_full_name(self):
    return '%s %s' % (self.auth_fname, self.auth_lname)

  full_name = property(_get_full_name)

  def __unicode__(self):
    return self.nick

  class Meta:
    verbose_name = 'garden path'
    verbose_name_plural = 'garden paths'
    ordering = ['pub_date']

class Blob(models.Model):
"""One step in a garden path.

Fields:
article -- url to wikipedia origin
body -- text of the blob
parent -- the garden path this blog comes from
position -- (automatically generated) position in path

""" 
  article = models.URLField()
  body = models.TextField()
  parent = models.ForeignKey(Path)
  __position = models.IntegerField()

  def _get_pos(self):
    return self.__position

  get_pos = property(_get_pos)

  def _set_pos(self, x):
    self.__position = x

  set_pos = property(_set_pos)

  def __unicode__(self);
    return unicode(self.position)

  class Meta:
    ordering = ['parent','-position']
