from .serializers import *
from lstm_api.models import User, BabyProfile, LifeLog, UserBabyRelationship

from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response

from django.db.models import Q

from django.utils import timezone

class LifeLogInfoViewSet(viewsets.ModelViewSet):
    '''
    아기의 일상생활을 기록 및 확인할 수 있도록 하는 class이다.
    '''

    queryset = LifeLog.objects.all()
    serializer_class = LifeLogInfoSerializer
    
    # 일상생활 기록을 리스팅한다.
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 특정 아이의 일상생활 기록을 리스팅한다.
    def list_specific(self, request, *args, **kwargs):
        if request.data['flag'] == True:
            relation_info = UserBabyRelationship.objects.filter(
                                    Q(user_id=request.user.id) &
                                    Q(baby_id=request.data['babyid']))
        else:
            relation_info = UserBabyRelationship.objects.filter(
                                    user_id=request.user.id)
       
        relation_ids = [x.id for x in relation_info]

        life_info = LifeLog.objects.filter(userbaby_relation__in = relation_ids)

        serializer = self.serializer_class(life_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 일상생활 기록을 등록한다.
    def set(self, request, *args, **kwargs):
        relation_info = generics.get_object_or_404(
                                    UserBabyRelationship,
                                    Q(user_id=request.user.id) &
                                    Q(baby_id=request.data['babyid']))
        
        serializer = self.serializer_class(data=request.data)
        
        if not serializer.is_valid():
            return Response({'result': 'failed', 'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if not request.user:
            return Response({'result': 'failed', 'error': 'User not authenticated'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        obj = serializer.save()
        obj.user = request.user
        obj.date = timezone.now()
        obj.userbaby_relation = relation_info
        obj.save()
        
        return Response({'result': 'success', 'success_id': obj.id}, status=status.HTTP_200_OK)

    # 특정 일상생활 기록을 검색한다.
    def retrieve(self, request, *args, **kwargs):
        life_info = LifeLog.objects.get(baby_id=kwargs["babyid"])
        serializer = self.serializer_class(life_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
