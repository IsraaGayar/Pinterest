from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = [
    ('F', 'Female'),
    ('M', 'Male'),
]

class User(AbstractUser):
    gender = models.CharField(choices= GENDER_CHOICES, max_length=50, null=True,blank=True )
    website = models.URLField(max_length=50,null=True,blank=True)
    short_bio = models.TextField(max_length=250,null=True,blank=True)
    profile_picture = models.ImageField(upload_to='photos',null=True,blank=True)
    follower = models.ManyToManyField(
        to='self',
        related_name='following',
        symmetrical=False,
        blank=True
    )
    savedPins = models.ManyToManyField('pins.Pin',related_name='savers',null=True,blank=True)

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.username

