from rest_framework import serializers
from .models import State, Location

class StateSerializer(serializers.HyperlinkedModelSerializer):
    locations = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        many=True,
        read_only=True
    )

    class Meta: 
        model = State
        fields = ('id', 'name', 'img_icon', 'average_daily_cases','locations',)

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    states = serializers.HyperlinkedRelatedField(
        view_name='state_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Location
        fields = ('id', 'name', 'business_name', 'business_img', 'address', 'hours', 'contact_number', 'offers', 'states',)