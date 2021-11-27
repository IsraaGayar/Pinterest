from rest_framework import serializers
from accounts.models import User


class UserListSerializer(serializers.ModelSerializer):
    url= serializers.HyperlinkedIdentityField(view_name='accounts:profile')
    class Meta:
        model = User
        fields = ['url', 'username', 'profile_picture']


class ProfileSerializer(serializers.ModelSerializer):
    pins = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pins:pindetails'
    )
    follower_count = serializers.IntegerField(
        source='follower.count',
        read_only=True
    )
    following_count=serializers.IntegerField(
        source='following.count',
        read_only=True
    )
    class Meta:
        model = User
        fields=['id','username','pins','follower_count','following_count']

class AccountSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(write_only=True)
    url= serializers.HyperlinkedIdentityField(view_name='accounts:profile',read_only=True)
    class Meta:
        model = User
        fields=['url',
                'username',
                'first_name',
                'last_name',
                'email',
                'gender',
                'website',
                'short_bio',
                'profile_picture',
                ]
