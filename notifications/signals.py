from django.db.models.signals import post_save
from django.dispatch import receiver
from comments.models import Comment,Like
from .models import Notification

@receiver(post_save, sender=Comment)
def usercreateHandler(sender,instance,created,**prams):
    if created:
        Notification.objects.create(
            content='someone commented on your post ',
            type='comment',
            owner = instance.pin.owner,
            notifier=instance.owner,
            pin=instance.pin,
        )

@receiver(post_save, sender=Like)
def usercreateHandler(sender,instance,created,**prams):
    if created:
        Notification.objects.create(
            content='someone liked on your post ',
            type='Like',
            owner = instance.pin.owner,
            notifier=instance.owner,
            pin=instance.pin,
        )
