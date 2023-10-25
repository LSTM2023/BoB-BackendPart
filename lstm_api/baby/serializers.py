from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from lstm_api.models import BabyProfile, UserBabyRelationship

class BabyInfoSerializer(serializers.ModelSerializer):
    # 아이의 정보를 다루기 위한 Serializer
    class Meta:
        model = BabyProfile
        fields = ('baby_name', 'birth', 'gender', 'url')

#class BabySetSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = BabyProfile
#        fields = ('baby_name', 'birth', 'gender', 'url')

class BabyRearerSerializer(serializers.ModelSerializer):
    # 아이와 유저의 관계를 다루기 위한 Serializer
    class Meta:
        model = UserBabyRelationship
        fields = ('baby', 'relation', 'access_date', 'access_starttime', 'access_endtime', 'active')

    def get_babies(self, validated_data):
        print(validated_data)

class BabyRearerListSerializer(serializers.ModelSerializer):
    # 특정 아이에 대한 모든 유저의 관계를 다루기 위한 Serializer
    class Meta:
        model = UserBabyRelationship
        fields = ('baby', 'user', 'relation', 'access_date', 'access_starttime', 'access_endtime', 'active')

