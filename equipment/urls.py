from django.urls import path
from.views import EquipList,EquipDetail


urlpatterns = [
    path('',EquipList.as_view(),name='equip_list'),
    path('<int:pk>/',EquipDetail.as_view(),name='equip_detail'),
]