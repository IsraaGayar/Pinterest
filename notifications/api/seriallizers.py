from rest_framework import serializers
from notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):

    notifier_username = serializers.CharField(source='notifier.username',read_only=True)
    notifier_pp=serializers.SerializerMethodField(method_name= 'get_profilePic')
    pin_title= serializers.CharField(source='pin.title',read_only=True)


    def get_profilePic(self, obj):
        try:
            image = obj.owner.profile_picture.url
        except ValueError:
            image = None  # we will put the default pic, or we will store it in the frontend to prevent reloading
        return image


    class Meta:
        model = Notification
        fields=[
            'notifier',
            'notifier_username',
            'type',
            'pin',
            'content',
            'notifier_pp',
            'pin_title',
        ]
