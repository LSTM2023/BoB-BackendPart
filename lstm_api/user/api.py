from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from lstm_api.models import User
from .serializers import UserSerializer, UserEditSerializer ,LoginSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from django.http import JsonResponse

@permission_classes([AllowAny])
class UserInfoViewSet(viewsets.ModelViewSet):
    '''
    유저의 정보를 확인하기 위한 class이다.
    여기서 fcm의 token을 수정 및 viewing할 수 있다.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    #등록된 유저 정보를 listing한다.
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 특정 User id의 유저 정보를 반환한다.
    def retrieve(self, request, *args, **kwargs):
        user_info = generics.get_object_or_404(User, id=kwargs['userid'])
        
        serializer.is_valid(raise_exception = True)
        serializer = self.serializer_class(user_info)
        return Response(serializer.data)
    
    # 특정 email의 유저 정보를 반환한다.
    def retrieve_by_email(self, request, *args, **kwargs):
        try:
            user_info = User.objects.get(email=request.data['email'])
        except:
            return Response("True", status=status.HTTP_200_OK) #legacy
        if user_info is None:
            return Response("True", status=status.HTTP_200_OK)
        else:
            return Response("False", status=status.HTTP_200_OK)

    # 특정 유저의 FCM Token을 반환한다.
    def user_token_retrieve(self, request, *args, **kwargs):
        user_info = generics.get_object_or_404(User, id=request.user.id)
        serializer = self.serializer_class(user_info)
        return Response(serializer.data['token'])

    # 특정 유저의 FCM token을 업데이트한다.
    def user_token_update(self, request, *args, **kwargs):
        user_info = User.objects.get(id=request.user.id)

        user_info.token = request.data["token"]

        user_info.save()

        return Response("Success", status=status.HTTP_200_OK)
    
    # Answer 답변을 통해 유저의 email을 찾는다.
    def user_find_email(self, request, *args, **kwargs):
        user_info = User.objects.get(id=request.user.id)

        if user_info.phone == request.data["phone"] and \
                user_info.qaAnswer == request.data["answer"]:
                    serializer = self.serializer_class(user_info)
                    return Response(serializer.data["email"])
        else:
            Response("Fail", status=status.HTTP_400_BAD_REQUEST)


class UserModifyViewSet(viewsets.ModelViewSet):
    '''
    유저 정보를 수정 및 삭제하기 위한 class이다.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # 특정 user id의 유저를 삭제한다.
    def remove(self, request, *args, **kwargs):
        user_info = generics.get_object_or_404(User, id=request.user.id)
        user_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 특정 user id의 유저 정보를 갱신한다.
    def edit(self, request, *args, **kwargs):
        user_info = User.objects.get(id=request.user.id)

        if "name" in request.data:
            user_info.name = request.data["name"]

        if "phone" in request.data:
            user_info.phone = request.data["phone"]

        if "qaType" in request.data:
            user_info.qatype = request.data["qaType"]
        if "qaAnswer" in request.data:
            user_info.qaAnswer = request.data["qaAnswer"]

        user_info.save()
        return Response("Success", status=status.HTTP_200_OK)

class UserLoginViewSet(viewsets.ModelViewSet):
    '''
    유저 로그인을 담당하는 class이다.
    로그인 이후엔 JWT Token을 발행해 Session 관리 및 인증을 수행한다.
    '''
    serializer_class = LoginSerializer
    
    # 유저는 로그인 시 email과 password로 로그인을 진행한다.
    def login(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)

        serializer.validate_username(request.data['email'])
        serializer.validate_username(request.data['password'])

    #def remove(self, request, *args, **kwargs):
    #    user_info = generics.get_object_or_404(User, id=request.user.id)
    #    user_info.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)
