from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    owner= serializers.HyperlinkedRelatedField(
                    read_only=True,
                    view_name='accounts:profile'
                )
    class Meta:
        model = Comment
        fields= ['content', 'owner', 'creationDate']