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
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields=[    'id',
                'username',
                'first_name',
                'last_name',
                'email',
                'gender',
                'website',
                'short_bio',
                'profile_picture',
                'password',
                'password2',
                ]
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username'),
            first_name = self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            email=self.validated_data.get('email'),
            gender=self.validated_data.get('gender'),
            website=self.validated_data.get('website'),
            short_bio=self.validated_data.get('short_bio'),
            profile_picture=self.validated_data.get('profile_picture'),
        )
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError(
                {
                    'password': "Password doesn't match"
                })
        else:
            user.set_password(self.validated_data.get('password'))
            user.save()