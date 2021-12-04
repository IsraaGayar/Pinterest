from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('accounts.User', related_name='boards', on_delete=models.CASCADE, default='')
    collaborator = models.ManyToManyField('accounts.User',related_name='BoardCollaborator',null=True,blank=True,default='')
    description= models.TextField(null=True, default='',blank=True)
    savedPins = models.ManyToManyField('pins.Pin',related_name='savers_boards',null=True,blank=True)
    createdat=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-createdat',)

    def __str__(self):
        return self.name