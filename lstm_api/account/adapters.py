from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    '''
    계정 등록 시 다른 데이터도 값을 담기 위한 Custom Adapter
    일반적인 데이터에 추가로 이름, 핸드폰, 질문 타입, 질문 정답을 등록한다.
    '''
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        
        user = super().save_user(request, user, form, False)
       
        user.name = request.data["name"]
        user.phone = request.data["phone"]
        user.qatype = request.data["qaType"]
        user.qaAnswer = request.data["qaAnswer"]

        user.save()
        return user
