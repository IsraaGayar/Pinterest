from rest_framework import generics

from notifications.api.seriallizers import NotificationSerializer
from notifications.models import Notification

class notifications(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(owner=user).all()


