from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from comments.models import Comment,Like
from accounts.models import User
from .models import Notification

@receiver(post_save, sender=Comment,weak=False)
def usercreateHandler(sender,instance,created,**prams):
    if created:
        Notification.objects.create(
            content='someone commented on your post ',
            type='comment',
            owner = instance.pin.owner,
            notifier=instance.owner,
            pin=instance.pin,
        )

@receiver(post_save, sender=Like,weak=False)
def usercreateHandler(sender,instance,created,**prams):
    if created:
        Notification.objects.create(
            content='someone liked on your post ',
            type='Like',
            owner = instance.pin.owner,
            notifier=instance.owner,
            pin=instance.pin,
        )
@receiver(m2m_changed, sender= User.follower.through,weak=False)
def follow(sender,instance,action,pk_set,*args,**kwargs):
    # instance= follower that was added (the one i added to my follower)
    if action=='pre_add':
        Notification.objects.create(
            content='someone followed you',
            type='follow',
            owner=User.objects.filter(pk__in=pk_set).first(),
            notifier=instance,
        )


