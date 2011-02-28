from django.db import models

class Path(models.Model):
  approval = False
  auth_email = models.EmailField()
  auth_fname = models.CharField(max_length=200)
  auth_lname = models.CharField(max_length=200)
  nick = models.SlugField()
  pub_date = models.DateTimeField('date published')
  title = models.CharField(max_length=300) 

  # change to python 2.6 to use this:
  # @property
  # def auth_name(self):
  #   return '%s %s' % (self.auth_fname, self.auth_lname)

  def _get_full_name(self):
    return '%s %s' % (self.auth_fname, self.auth_lname)

  auth_name = property(_get_full_name)

  def __unicode__(self):
    return self.nick

  class Meta:
    verbose_name = 'garden path'
    verbose_name_plural = 'garden paths'
    ordering = ['pub_date']

class Blob(models.Model):
  article = models.URLField()
  body = models.TextField()
  path = models.ForeignKey(Path)
  position = models.IntegerField()
 
  def __unicode__(self):
    return unicode(self.path) + "; " + unicode(self.position)

  class Meta:
    ordering = ['path','position']
