from .serializers import *
from lstm_api.user.serializers import UserSerializer 
from lstm_api.models import User, BabyProfile, UserBabyRelationship

from django.db.models import Q

from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response

class BabyInfoViewSet(viewsets.ModelViewSet):
    '''
    아기 정보를 생성, 확인, 수정, 삭제하는 View들이 구성되어 있는 클래스이다.
    BabyProfile의 Object를 다룬다.
    '''
    queryset = BabyProfile.objects.all()
    serializer_class = BabyInfoSerializer

    # 등록되어 있는 아기 list 확인
    def list(self, request, *args, **kwargs):
        #queryset = BabyProfile.objects.all()
        serializer = self.serializer_class(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 아기 등록
    def set(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        # 만약 유저가 인증되어 있지 않거나 serializer가 vaild하지 않다면 500에러
        if not serializer.is_valid():
            return Response({'result': 'failed', 'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if not request.user:
            return Response({'result': 'failed', 'error': 'User not authenticated'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        obj = serializer.save()
        obj.user = request.user
        obj.user_baby_rel.set([request.user])
        obj.save()
        
        return Response({'result': 'success', 'success_id': obj.id}, status=status.HTTP_200_OK)

    # 아기 정보 수정
    def modify(self, request, *args, **kwargs):
        baby_info = BabyProfile.objects.get(id=request.data["babyid"])
        
        if "baby_name" in request.data:
            baby_info.baby_name = request.data["baby_name"]

        if "gender" in request.data:
            baby_info.gender = request.data["gender"]

        if "birth" in request.data:
            baby_info.birth = request.data["birth"]
        
        baby_info.save()
        
        return Response({'result': 'success'} , status=status.HTTP_200_OK)

    # 아기 정보 검색
    def retrieve(self, request, *args, **kwargs):
        baby_info = BabyProfile.objects.get(id=kwargs["babyid"])
        serializer = self.serializer_class(baby_info)
        return Response(serializer.data)

    # 아기 정보 삭제
    def delete(self, request, *args, **kwargs):
        relation_info = UserBabyRelationship.objects.filter(baby_id=kwargs["babyid"])
        relation_info.delete()
        baby_info = BabyProfile.objects.get(id=kwargs["babyid"])
        baby_info.delete()

        return Response({'result': 'success'}, status=status.HTTP_200_OK)


class BabyRearer(viewsets.ModelViewSet):
    '''
    아기와 부모의 관계 정보를 생성, 확인, 수정, 삭제하는 View들이 구성되어 있는 클래스이다.
    UserBabyRelationship의 Object를 다룬다.
    '''
    queryset = UserBabyRelationship.objects.all()
    serializer_class = BabyRearerSerializer
    
    # 아기와 부모의 모든 관계를 listing한다.
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # 로그인 되어있는 유저와 아이의 관계를 listing한다.
    def list_specific(self, request, *args, **kwargs):
        babies_info = UserBabyRelationship.objects.filter(user_id=request.user.id)
        serializer = self.serializer_class(babies_info, many=True)
        return Response(serializer.data)
    
    # 특정 아이와 다른 모든 유저의 관계를 반환한다.
    def list_rearer(self, request, *args, **kwargs):
        babies_info = UserBabyRelationship.objects.filter(user_id=request.user.id)
        serializer = BabyRearerListSerializer(babies_info, many=True)
        
        babies_id_list = [x["baby"] for x in serializer.data]

        relationship_list = UserBabyRelationship.objects.filter(baby_id__in=babies_id_list)
        serializer_x = BabyRearerListSerializer(relationship_list, many=True)

        return Response("Success", status=status.HTTP_200_OK)
    
    # 부모와 아이의 관계를 설정한다.
    def set(self, request, *args, **kwargs):
        user_info = User.objects.filter(email=request.data['email'])
        
        user_serializer = UserSerializer(user_info, many=True)

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({'result': 'failed', 'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if not request.user:
            return Response({'result': 'failed', 'error': 'User not authenticated'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        obj = serializer.save()
        obj.user = request.user
        obj.user_id = user_serializer.data[0]['id']
        obj.active = False
        obj.save()

        return Response({'result': 'success', 'success_id': obj.id}, status=status.HTTP_200_OK)
    
    # 부모가 베이비시터의 아기 정보 접근을 허용한다.
    def activate(self, request, *args, **kwargs):
        relation_info = generics.get_object_or_404(
                                    UserBabyRelationship, 
                                    Q(user_id=request.user.id) &
                                    Q(baby_id=request.data['babyid']))

        relation_info.active = True
        relation_info.save()

        return Response({'result': 'success'}, status=status.HTTP_200_OK)

    
    def retrieve(self, request, *args, **kwargs):
        baby_info = BabyProfile.objects.get(id=kwargs["babyid"])
        serializer = self.serializer_class(baby_info)
        return Response(serializer.data)
