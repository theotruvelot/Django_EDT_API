from django.db import models


# Create your models here.
# create model for edt
class EdtWeek(models.Model):
    Semaine = models.IntegerField(unique=True)
    DebutSeance = models.DateTimeField()
    FinSeance = models.DateTimeField()


class Edt(models.Model):
    # matter
    CodeSeance = models.CharField(max_length=10)
    NomSession = models.CharField(max_length=100)
    NomMatiere = models.CharField(max_length=200)
    ThemeSeance = models.CharField(max_length=200)
    IntervenantNom = models.CharField(max_length=100)
    IntervenantPrenom = models.CharField(max_length=100)
    DebutSeance = models.DateTimeField()
    FinSeance = models.DateTimeField()
    NomSalle = models.CharField(max_length=100)
    Semaine = models.IntegerField()

    ## get foreign key from edtweek



