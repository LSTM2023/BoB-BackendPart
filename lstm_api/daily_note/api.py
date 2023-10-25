from .serializers import *
from lstm_api.models import User, BabyProfile, DailyNote, UserBabyRelationship

from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response

from django.db.models import Q

from django.utils import timezone

class DailyNoteInfoViewSet(viewsets.ModelViewSet):
    '''
    일일 일기에 대한 정보를 다루는 클래스이다.
    UserBabyRelationship에서 로그인한 유저와 아이의 관계 정보를 가져온 뒤
    DailyNote에서 해당 데이터를 바탕으로 일기를 처리한다.
    '''
    queryset = DailyNote.objects.all()
    serializer_class = DailyNoteInfoSerializer

    # 등록된 일기를 listing 한다.
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 특정 일기를 리스팅한다.
    def list_specific(self, request, *args, **kwargs):
        # flag가 True일 경우 로그인 된 유저의 특정 아이의 일기를 리스팅한다.
        if request.data['flag'] == True:
            relation_info = UserBabyRelationship.objects.filter(
                                    Q(user_id=request.user.id) &
                                    Q(baby_id=request.data['babyid']))
        # 만약 flag가 false일 경우 로그인 된 유저의 일기를 리스팅한다.
        else:
            relation_info = UserBabyRelationship.objects.filter(
                                    user_id=request.user.id)
        relation_ids = [x.id for x in relation_info]

        note_info = DailyNote.objects.filter(userbaby_relation__in = relation_ids)

        serializer = self.serializer_class(note_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 작성한 일기를 저장한다.
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
        #obj.photo = request.FILES['photo']
        #obj.date = timezone.now()
        obj.userbaby_relation = relation_info
        obj.save()

        return Response({'result': 'success', 'success_id': obj.id}, status=status.HTTP_200_OK)
    
    # 특정 날짜에 등록된 일기를 확인한다.
    def retrieve(self, request, *args, **kwargs): 
        relation_info = UserBabyRelationship.objects.filter(
                                    Q(user_id=request.user.id) &
                                    Q(baby_id=request.data['babyid']))

        relation_ids = [x.id for x in relation_info]

        daily_info = DailyNote.objects.filter(
                            Q(userbaby_relation__in = relation_ids) &
                            Q(date=request.data['date']))

        serializer = self.serializer_class(daily_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 특정 일기를 수정한다.
    def edit(self, request, *args, **kwargs):
        relation_info = UserBabyRelationship.objects.get(
                            Q(user_id=request.user.id) &
                            Q(baby_id=request.data['babyid']))
        
        daily_info = DailyNote.objects.get(
                            Q(userbaby_relation = relation_info) &
                            Q(date=request.data['date']))

        if "title" in request.data:
            daily_info.title = request.data["title"]

        if "content" in request.data:
            daily_info.content = request.data["content"]

        if "photo" in request.data:
            daily_info.photo = request.data["photo"]

        daily_info.save()

        return Response({'result': 'success'} , status=status.HTTP_200_OK) 
    
    # 특정 일기를 삭제한다.
    def delete(self, request, *args, **kwargs):
        relation_info = UserBabyRelationship.objects.get(
                            Q(user_id=request.user.id) &
                            Q(baby_id=request.data['babyid']))

        daily_info = DailyNote.objects.get(
                            Q(userbaby_relation = relation_info) &
                            Q(date=request.data['date']))

        daily_info.delete()

        return Response({'result': 'success'} , status=status.HTTP_200_OK)
