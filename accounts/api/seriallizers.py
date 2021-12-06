from rest_framework import serializers
from django.contrib.auth import get_user_model

from boards.api.seriallizers import boardSerializer
from pins.api.seriallizers import Pinintro

User = get_user_model()


def is_user_followed(self, obj):
    try:
        request = self.context.get("request")
        user = request.user
        if obj in user.follower.all():
            case = True
        else:
            case = False
    except:
        case = False
    return case


class UserListSerializer(serializers.ModelSerializer):
    url= serializers.HyperlinkedIdentityField(view_name='accounts:profile')
    is_follow = serializers.SerializerMethodField(method_name='is_followed')

    def is_followed(self, obj):
        return is_user_followed(self, obj)

    class Meta:
        model = User
        fields = ['url', 'username', 'profile_picture','is_follow']


class ProfileSerializer(serializers.ModelSerializer):
    pins= Pinintro(many=True, read_only=True)
    savedPins=Pinintro(many=True, read_only=True)
    boards = boardSerializer(many=True)
    follower_count = serializers.IntegerField(
        source='following.count',
        read_only=True
    )
    following_count=serializers.IntegerField(
        source='follower.count',
        read_only=True
    )
    is_follow = serializers.SerializerMethodField(method_name='is_followed')

    def is_followed(self, obj):
        return is_user_followed(self, obj)

    class Meta:
        model = User
        fields=['id',
                'username',
                'pins',
                'profile_picture',
                'follower_count',
                'following_count',
                'boards',
                'savedPins',
                'is_follow']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id',
                'username',
                'first_name',
                'last_name',
                'email',
                'gender',
                'website',
                'short_bio',
                'profile_picture',
                ]
class ProfilePic(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=[
                'profile_picture',
                ]
class ownerInfoSerializer(serializers.ModelSerializer):
    is_follow = serializers.SerializerMethodField(method_name='is_followed')

    def is_followed(self, obj):
        return is_user_followed(self, obj)
    class Meta:
        model = User
        fields=['id',
                'username',
                'profile_picture',
                'is_follow'
                ]


class RegisterationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            # 'email',
            'username', 'password', 'password_confirm']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {
                    'password': "Password doesn't match"
                }
            )

        user = User(
            # email=self.validated_data.get('email'),
            username=self.validated_data.get('username'),
        )
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user






    # def create(self, validated_data):
    #     user=User.objects.create(**validated_data)
    #     print(user.password)
    #     user.set_password(self.validated_data.get('password'))
    #     print(user.password)
    #     user.save()
    #     return user

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance
    #
    # def save(self, **kwargs):
    #     user = User(
    #         username=self.validated_data.get('username'),
    #         first_name = self.validated_data.get('first_name'),
    #         last_name=self.validated_data.get('last_name'),
    #         email=self.validated_data.get('email'),
    #         gender=self.validated_data.get('gender'),
    #         website=self.validated_data.get('website'),
    #         short_bio=self.validated_data.get('short_bio'),
    #         profile_picture=self.validated_data.get('profile_picture'),
    #     )
    #     if self.validated_data.get('password') != self.validated_data.get('password2'):
    #         raise serializers.ValidationError(
    #             {
    #                 'password': "Password doesn't match"
    #             })
    #     else:
    #         user.set_password(self.validated_data.get('password'))
    #         user.save()