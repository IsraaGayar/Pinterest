from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('accounts.User', related_name='boards', on_delete=models.CASCADE, default='')
    collaborator = models.ManyToManyField('accounts.User',related_name='BoardCollaborator',blank=True,symmetrical=True,default='')
    # pin=models.ManyToManyField(Pin,null=True)
    savedPins = models.ManyToManyField('pins.Pin',related_name='savers_boards',null=True,blank=True)

    def __str__(self):
        return self.name