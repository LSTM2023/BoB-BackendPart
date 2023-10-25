from .serializers import *
from lstm_api.models import BabyProfile, GrowthLog 

from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from django.utils import timezone

class GrowthLogInfoViewSet(viewsets.ModelViewSet):
    '''
    아기의 성장 정보를 다루는 class이다.
    '''
    queryset = GrowthLog.objects.all()
    serializer_class = GrowthLogInfoSerializer
    
    # 아기의 성장 정보를 리스팅한다.
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 아기의 성장 정보를 등록한다.
    def set(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({'result': 'failed', 'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if not request.user:
            return Response({'result': 'failed', 'error': 'User not authenticated'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        obj = serializer.save()
        obj.user = request.user
        #obj.date = request.POST.get("date", default=timezone.now())
        obj.save()
        
        return Response({'result': 'success', 'success_id': obj.id}, status=status.HTTP_200_OK)

    # 아기의 성장 정보를 검색한다.
    def retrieve(self, request, *args, **kwargs):
        growth_info = GrowthLog.objects.filter(baby_id=kwargs["babyid"])
        serializer = self.serializer_class(growth_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
