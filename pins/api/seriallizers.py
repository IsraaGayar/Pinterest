from rest_framework import serializers

from comments.api.seriallizers import CommentSerializer
from pins.models import Pin

#pinList
class PinSerializer(serializers.ModelSerializer):
    owner_username=serializers.CharField(source='owner.username',read_only=True)
    comments= CommentSerializer(many=True,read_only=True)
    likes = serializers.IntegerField(
        source='pinlikes.count',
        read_only=True
    )
    profilePic=serializers.SerializerMethodField(method_name= 'get_profilePic')

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
                 'owner',
                 'owner_username',
                 'profilePic',
                 'comments',
                 'tags',
                 'likes']
        extra_kwargs = {'owner': {'read_only': True}}


#pinList
class Pinintro(serializers.ModelSerializer):
    url= serializers.HyperlinkedIdentityField(view_name='pins:pindetails')

    class Meta:
        model = Pin
        fields= ['url',
                 'pin_picture',
                 'id',
                 ]


class PinListSerializer(serializers.ModelSerializer):
    owner= serializers.HyperlinkedRelatedField(
                    read_only=True,
                    view_name='accounts:profile'
                )
    url= serializers.HyperlinkedIdentityField(view_name='pins:pindetails')
    ownerName=serializers.SerializerMethodField(method_name= 'get_ownerName')

    def get_ownerName(self,obj):
        return obj.owner.username


    class Meta:
        model = Pin
        fields= ['url',
                 'id',
                 'title',
                 'owner',
                 'pin_picture',
                 'ownerName',
                 ]
