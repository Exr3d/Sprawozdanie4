from django.db import models

# Create your models here.

class Karty_Graficzne(models.Model):
    Marka = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    VRAM = models.IntegerField(max_length=5)
    avgCena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Marka + " " + self.Model + " "
