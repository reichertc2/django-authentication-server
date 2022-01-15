from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Equip
from .serializers import EquipSerializer
from .permissions import IsInspectorOrReadOnly


class EquipList(ListCreateAPIView):
    queryset = Equip.objects.all()
    model = Equip
    serializer_class = EquipSerializer

class EquipDetail(RetrieveUpdateDestroyAPIView):
    query_set = Equip.objects.all()
    model = Equip
    serializer_class = EquipSerializer
    permission_classes = (IsInspectorOrReadOnly,)
