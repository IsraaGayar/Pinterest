from django.db import models

LIKES_CHOICES = (
    {'H', 'Heart'},
    {'L', 'Like'},
    {'J', 'Joyful'},
    {'H', 'Haha'},
)
class Comment(models.Model):
    content = models.TextField(max_length=500)
    pin = models.ForeignKey('pins.Pin',related_name='comments',on_delete=models.CASCADE)
    owner= models.ForeignKey('accounts.User',related_name='comments',on_delete=models.CASCADE)
    creationDate = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['creationDate']

    def __str__(self):
        return self.content

class Like(models.Model):
    type  = models.CharField(max_length=500, choices= LIKES_CHOICES )
    pin = models.ForeignKey('pins.Pin', related_name='pinlikes', on_delete=models.CASCADE,default='')
    owner = models.ForeignKey('accounts.User', related_name='likes', on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.type