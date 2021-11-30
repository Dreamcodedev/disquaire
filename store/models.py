from django.db import models

# Create your models here.
from django.db import models

class Artist(models.Model):
  name=models.CharField('Artiste',max_length=200, unique=True)

  class Meta :
    verbose_name= "artiste"

  def __str__(self):
    return self.name



class Contact(models.Model):
    email = models.EmailField('Email',max_length=100)
    name = models.CharField('Nom du propect',max_length=200)

    class Meta :
      verbose_name= "prospect"

    def __str__(self):
      return self.name


class Album(models.Model):
    reference = models.IntegerField('référence', blank=True, null=True)
    created_at = models.DateTimeField('Date de création',auto_now_add=True)
    available = models.BooleanField('disponibilité',default=True)
    title = models.CharField('titre',max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    class Meta :
      verbose_name= "disque"

    def __str__(self):
      return self.title


class Booking(models.Model):
    created_at = models.DateTimeField('Date de création', auto_now_add=True)
    contacted = models.BooleanField('Prospecté',default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta :
      verbose_name= "reservation"

    def __str__(self):
      return self.contact.name
