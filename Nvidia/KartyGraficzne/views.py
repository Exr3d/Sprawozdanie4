from .models import Karty_Graficzne
from rest_framework import viewsets
from .serializer import KartySerializer

class KartyViewSet(viewsets.ModelViewSet):
    queryset = Karty_Graficzne.objects.all()
    serializer_class = KartySerializer
