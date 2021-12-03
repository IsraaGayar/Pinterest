from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    profilePic = serializers.SerializerMethodField(method_name='get_profilePic')

    def get_profilePic(self, obj):
        try:
            image = obj.owner.profile_picture.url
        except ValueError:
            image = None  # we will put the default pic, or we will store it in the frontend to prevent reloading
        return image

    class Meta:
        model = Comment
        fields = ['content',
                  'owner',
                  'owner_username',
                  'creationDate',
                  'profilePic']
        extra_kwargs = {'owner': {'read_only': True}}
