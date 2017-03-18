from rest_framework import viewsets
from whatsapp.serializers import DataSerializer
from whatsapp.models import Data


class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MD to hack.
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
