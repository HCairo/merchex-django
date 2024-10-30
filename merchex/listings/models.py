from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        POP = 'PO'
        ROCK = 'RO'
        RNB = 'RB'
        ELECTRONIC = 'ED'
        COUNTRY = 'CO'
        REGGAE = 'RE'
        JAZZ = 'JA'
        CLASSICAL = 'CL'
        METAL = 'ME'
        SOUL = 'SO'
        BLUES = 'BL'
        K_POP = 'KP'
        LATINO = 'LA'
        FOLK = 'FO'
        GOSPEL = 'GO'
        PUNK = 'PU'
        DISCO = 'DI'
        REGGAETON = 'RG'
        AFROBEATS = 'AF'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices ,max_length=10)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS = 'RC'
        CLOTHING = 'CL'
        POSTERS = 'PS'
        MISCELLANEOUS = 'MS'

    name = models.fields.CharField(max_length=100)
    type = models.fields.CharField(choices=Type.choices ,max_length=10)
    year = models.fields.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2024)], null=True, blank=True)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.name}'