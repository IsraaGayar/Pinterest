from rest_framework import serializers

from comments.api.seriallizers import CommentSerializer
from pins.models import Pin


def is_pin_saved(self, obj):
    try:
        request = self.context.get("request")
        user = request.user
        if obj in user.savedPins.all():
            case = True
        else:
            case = False
    except:
        case = False
    return case
def is_user_followed(self, obj):
    try:
        request = self.context.get("request")
        user = request.user
        if obj.owner in user.follower.all():
            case = True
        else:
            case = False
    except:
        case = False
    return case


#pinList
class PinSerializer(serializers.ModelSerializer):
    owner_username=serializers.CharField(source='owner.username',read_only=True)
    comments= CommentSerializer(many=True,read_only=True)
    likes = serializers.IntegerField(
        source='pinlikes.count',
        read_only=True
    )
    profilePic=serializers.SerializerMethodField(method_name= 'get_profilePic')
    pin_saved=serializers.SerializerMethodField(method_name='is_saved')
    is_follow = serializers.SerializerMethodField(method_name='is_followed')

    def is_followed(self, obj):
        return is_user_followed(self, obj)

    def is_saved(self, obj):
        return is_pin_saved(self, obj)

    def get_profilePic(self, obj):
        try:
            image = obj.owner.profile_picture.url
        except ValueError:
            image = None  # we will put the default pic, or we will store it in the frontend to prevent reloading
        return image

    class Meta:
        model = Pin
        fields= ['id',
                 'title',
                 'description',
                 'alt_description',
                 'pin_picture',
                 'destination_link',
                 'pin_saved',
                 'owner',
                 'is_follow',
                 'owner_username',
                 'profilePic',
                 'comments',
                 'tags',
                 'likes']
        extra_kwargs = {'owner': {'read_only': True}}


#pinList
class Pinintro(serializers.ModelSerializer):
    url= serializers.HyperlinkedIdentityField(view_name='pins:pindetails')
    pin_saved=serializers.SerializerMethodField(method_name='is_saved')

    def is_saved(self,obj):
        return is_pin_saved(self, obj)

    class Meta:
        model = Pin
        fields= ['url',
                 'pin_picture',
                 'id',
                 'pin_saved',
                 'title',
                 ]


class PinListSerializer(serializers.ModelSerializer):
    # request = self.context.get("request")
    owner= serializers.HyperlinkedRelatedField(
                    read_only=True,
                    view_name='accounts:profile'
                )
    url= serializers.HyperlinkedIdentityField(view_name='pins:pindetails')
    ownerName=serializers.SerializerMethodField(method_name= 'get_ownerName')
    pin_saved=serializers.SerializerMethodField(method_name='is_saved')

    def get_ownerName(self,obj):
        return obj.owner.username
    def is_saved(self,obj):
        return is_pin_saved(self, obj)

    class Meta:
        model = Pin
        fields= ['url',
                 'id',
                 'title',
                 'owner',
                 'pin_picture',
                 'ownerName',
                 'pin_saved',
                 ]
