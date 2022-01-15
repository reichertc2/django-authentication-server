from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Equip
from .serializers import EquipSerializer
from .permissions import IsInspectorOrReadOnly


class EquipList(ListCreateAPIView):
    queryset = Equip.objects.all()
    serializer_class = EquipSerializer

class EquipDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsInspectorOrReadOnly,)
    query_set = Equip.objects.all()
    serializer_class = EquipSerializer