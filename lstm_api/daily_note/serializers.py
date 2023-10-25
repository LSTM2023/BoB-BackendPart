from rest_framework import serializers, exceptions
from lstm_api.models import BabyProfile, DailyNote 

class DailyNoteInfoSerializer(serializers.ModelSerializer):
    #photo = serializers.ImageField(use_url=True)
    class Meta:
        model = DailyNote
        #fields = '__all__'
        fields = ('userbaby_relation', 'date', 'title', 'content', 'photo')
