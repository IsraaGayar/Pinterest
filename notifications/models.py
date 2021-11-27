from django.db import models


class Notification(models.Model):
    content  = models.TextField(max_length=500)
    creation_date = models.DateField(auto_now_add=True)
    type  = models.CharField(max_length=500, default='')
    owner= models.ForeignKey('accounts.User',related_name='notifications',on_delete=models.CASCADE,default='')
    notifier= models.ForeignKey('accounts.User',related_name='sentNotifications',on_delete=models.CASCADE,default='')
    pin= models.ForeignKey('pins.Pin',related_name='notifications',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.content