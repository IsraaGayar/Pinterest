from rest_framework import serializers
from notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):

    notifier_username = serializers.CharField(source='notifier.username',read_only=True)

    class Meta:
        model = Notification
        fields=[
            'notifier',
            'notifier_username',
            'type',
            'pin',
            'content',
        ]
