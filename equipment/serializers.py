from rest_framework import serializers
from .models import Equip

class EquipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equip
        fields = ('id','name','description','manufacturer','inspector',)