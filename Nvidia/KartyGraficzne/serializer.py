from .models import Karty_Graficzne
from rest_framework import serializers

class KartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Karty_Graficzne
        fields = ['id', 'Marka', 'Model', 'VRAM', 'avgCena', 'czestotliwosc']