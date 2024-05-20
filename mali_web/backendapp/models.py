from django.contrib.gis.db import models as gis_models
from django.db import models


# class Region(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     #habitats = models.IntegerField()
#     def __str__(self):
#         return self.name

# pour Bamako
class Bamako(models.Model):
    habitats = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return "Bamako"

# pour Gao
class Gao(models.Model):
    habitats = models.IntegerField()

    def __str__(self):
        return "Gao"

# pour Kidal
class Kidal(models.Model):
    habitats = models.IntegerField()

    def __str__(self):
        return "Kidal"

# pour Koulikoro
class Koulikoro(models.Model):
    habitats = models.IntegerField()

    def __str__(self):
        return "Koulikoro"

# pour Mopti
class Mopti(models.Model):
    habitats = models.IntegerField()

    def __str__(self):
        return "Mopti"

# pour Ségou
class Ségou(models.Model):
    habitats = models.IntegerField()

    def __str__(self):
        return "Ségou"

# pour Sikasso
class Sikasso(models.Model):
    habitats = models.IntegerField()

    def __str__(self):
        return "Sikasso"

# pour Timbuktu
class Timbuktu(models.Model):
    habitats = models.IntegerField()

    def __str__(self):
        return "Timbuktu"

# pour Kayes
class Kayes(models.Model):
    habitats = models.IntegerField()

    def __str__(self):
        return "Kayes"
