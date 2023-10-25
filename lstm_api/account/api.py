from dj_rest_auth.registration.views import LoginView
from rest_framework import viewsets, permissions, generics, status

from lstm_api.models import User
from lstm_api.user.serializers import UserSerializer

from allauth.account.adapter import DefaultAccountAdapter

class CustomLoginView(LoginView):
    '''
    Login 시 유저의 정보 및 JWT Token을 반환하기 위한 
    Custom Login View
    '''
    def get_response(self):
        orginal_response = super().get_response()
        
        mydata = {"message": "Done", "status": "success"}
        
        user_info = generics.get_object_or_404(User, id=int(orginal_response.data['user']['pk']))

        serializer = UserSerializer(user_info)
        
        orginal_response.data.update(mydata)
        orginal_response.data.update(serializer.data)
        
        return orginal_response
