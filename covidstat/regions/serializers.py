from rest_framework import serializers
# from rest_framework.validators import UniqueTogetherValidator
# from rest_framework.decorators import action
# from rest_framework.response import Response
#
# import datetime as dt

from .models import REGIONS, Region


class RegionSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateField()
    region = serializers.ChoiceField(choices=REGIONS)
    sick = serializers.IntegerField()
    died = serializers.IntegerField()
    sick_today = serializers.IntegerField()
    died_today = serializers.IntegerField()


    class Meta:
        model = Region
        fields = ('pub_date', 'region', 'sick', 'died', 'sick_today', 'died_today')

    def create(self, validated_data):
        return Region.objects.create(**validated_data)
