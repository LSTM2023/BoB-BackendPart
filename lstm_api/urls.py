from django.urls import path, include

from lstm_api.account import api as account_api
from lstm_api.user import api as user_api
from lstm_api.baby import api as baby_api
from lstm_api.life_log import api as lifelog_api
from lstm_api.growth_log import api as growthlog_api
from lstm_api.health_check import api as health_check_api
from lstm_api.daily_note import api as daily_note_api

urlpatterns = [
        # 유저 계정 관련 API List
        path('user/login/', account_api.CustomLoginView.as_view()),
        path('user/exist/', user_api.UserInfoViewSet.as_view({'post': 'retrieve_by_email'})),
        path('user/edit/', user_api.UserModifyViewSet.as_view({'post': 'edit'})),
        path('user/', include('dj_rest_auth.urls')),
        path('user/registration/', include('dj_rest_auth.registration.urls')),
        path('user/remove/', user_api.UserModifyViewSet.as_view({'get': 'remove'})),
        path('user/ftoken/retrieve/', user_api.UserInfoViewSet.as_view({'get': 'user_token_retrieve'})),
        path('user/ftoken/update/', user_api.UserInfoViewSet.as_view({'post': 'user_token_update'})),
        path('user/find/email/', user_api.UserInfoViewSet.as_view({'post': 'user_find_email'})),
        
        # 아기 정보 관련 API List
        path('baby/list/', baby_api.BabyInfoViewSet.as_view({'get': 'list'})),
        path('baby/set/', baby_api.BabyInfoViewSet.as_view({'post': 'set'})),
        path('baby/<int:babyid>/get/', baby_api.BabyInfoViewSet.as_view({'post': 'retrieve'})),
        path('baby/<int:babyid>/delete/', baby_api.BabyInfoViewSet.as_view({'get': 'delete'})),
        path('baby/modify/', baby_api.BabyInfoViewSet.as_view({'post': 'modify'})),
        
        # 아기와 유저의 관계 관련 API List
        path('baby/lists/', baby_api.BabyRearer.as_view({'post': 'list_specific'})),
        path('baby/connect/', baby_api.BabyRearer.as_view({'post': 'set'})),
        path('baby/rearer/', baby_api.BabyRearer.as_view({'post': 'list_rearer'})),
        path('baby/activate/', baby_api.BabyRearer.as_view({'post': 'activate'})),
        
        # 아기의 일상생활를 기록할 수 있는 API List
        path('life/list/', lifelog_api.LifeLogInfoViewSet.as_view({'get': 'list'})),
        path('life/lists/', lifelog_api.LifeLogInfoViewSet.as_view({'post': 'list_specific'})),
        path('life/set/', lifelog_api.LifeLogInfoViewSet.as_view({'post': 'set'})),
        path('life/<int:babyid>/get/', lifelog_api.LifeLogInfoViewSet.as_view({'post': 'retrieve'})),
        
        # 아이의 성장 정보를 기록할 수 있는 API List
        path('growth/list/', growthlog_api.GrowthLogInfoViewSet.as_view({'get': 'list'})),
        path('growth/set/', growthlog_api.GrowthLogInfoViewSet.as_view({'post': 'set'})),
        path('growth/<int:babyid>/get/', growthlog_api.GrowthLogInfoViewSet.as_view({'post': 'retrieve'})),
        
        # 아이의 건강검진/예방접종 내역을 기록할 수 있는 API List
        path('health/list/', health_check_api.HealthCheckInfoViewSet.as_view({'get': 'list'})),
        path('health/set/', health_check_api.HealthCheckInfoViewSet.as_view({'post': 'set'})),
        path('health/<int:babyid>/get/', health_check_api.HealthCheckInfoViewSet.as_view({'post': 'retrieve'})),
        
        # 아이의 일기를 기록할 수 있는 API List
        path('daily/list/', daily_note_api.DailyNoteInfoViewSet.as_view({'get': 'list'})),
        path('daily/lists/', daily_note_api.DailyNoteInfoViewSet.as_view({'post': 'list_specific'})),
        path('daily/set/', daily_note_api.DailyNoteInfoViewSet.as_view({'post': 'set'})),
        path('daily/get/', daily_note_api.DailyNoteInfoViewSet.as_view({'post': 'retrieve'})),
        path('daily/edit/', daily_note_api.DailyNoteInfoViewSet.as_view({'post': 'edit'})),
        path('daily/delete/', daily_note_api.DailyNoteInfoViewSet.as_view({'post': 'delete'})),
    ]
