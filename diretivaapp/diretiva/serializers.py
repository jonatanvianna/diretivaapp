from rest_framework import serializers
from .models import Diretiva


class DiretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretiva
        fields = ('id', 'date_entry', 'status', 'main_ticket', 'product', 'description', 'date_update', 'date_closed')
