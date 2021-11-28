from django.db import models

# Create your models here.
class Pin(models.Model):
    title= models.CharField(max_length=50)
    description= models.TextField(null=True, default='')
    alt_description= models.CharField(max_length=250, null=True, default='')
    pin_picture = models.ImageField(upload_to='photos', null=True, blank=True)
    destination_link = models.URLField(max_length=200, null=True, blank=True)
    createdat=models.DateTimeField(auto_now_add=True)
    owner= models.ForeignKey('accounts.User',related_name='pins',on_delete=models.CASCADE)
    tags=models.ManyToManyField('Tag',related_name='pins',blank=True)

    class Meta:
        ordering = ('-createdat',)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
