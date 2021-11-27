from django.contrib import admin
from .models import Pin,Tag

# Register your models here.

class customPin(admin.ModelAdmin):

    list_display = ('title', 'owner')
    search_fields = ['tags__name']

admin.site.register(Tag)
admin.site.register(Pin,customPin)
