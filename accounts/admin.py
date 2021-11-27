from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User



class CustomUserAdmin(UserAdmin):
    readonly_fields = ['getPins','getfollowing']
    list_display = ('username', 'first_name', 'last_name','getPins')

    fieldsets = (
        ('General Info', {'fields': ('username', 'password') }),
        # ('Personal info', {'fields': ('first_name', 'email','follower','savedPins' ,'getPins','getfollowing')}),
        ('User info', {'fields': (
                'first_name',
                'last_name',
                'email',
                'gender',
                'website',
                'short_bio',
                'profile_picture',
                'follower',
                'savedPins',
                'getPins',
                'getfollowing'
        )}),

        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        (None, {'fields': ('last_login', 'date_joined')}),
    )
    def getfollowing(self,obj):
        following=list(obj.following.all())
        return following

    def getPins(self, obj):
        mypins = list(obj.pins.all())
        return mypins

admin.site.register(User,CustomUserAdmin)
