from rest_framework import serializers
from whatsapp.models import Data

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('__all__')
