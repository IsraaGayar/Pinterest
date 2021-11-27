from rest_framework import serializers
from boards.models import Board
from pins.api.seriallizers import PinListSerializer


class boardSerializer(serializers.ModelSerializer):
    collaborator = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='userdetails'
    )
    savedPins= PinListSerializer(many=True,read_only=True)
    class Meta:
        model=Board
        fields='__all__'
