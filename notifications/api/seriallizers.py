from rest_framework import serializers
from notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='accounts:profile'
    )
    notifier = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='accounts:profile'
    )
    pin = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='pins:pindetails'
    )
    class Meta:
        model = Notification
        fields='__all__'
