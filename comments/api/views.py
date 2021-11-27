from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from comments.api.seriallizers import CommentSerializer
from comments.models import Comment, Like
from pins.models import Pin


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user,pin=Pin.objects.get(pk=self.kwargs['pk']))
        except:
            pass


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def LikePin(request,*args,**kwargs):
    try:
        Like.objects.create(
            owner=request.user,
            type=kwargs['liketype'],
            pin=Pin.objects.get(pk=kwargs['pk']),
        )
    except:
        return Response(data={'message': 'bad request'},status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unLikePin(request,*args,**kwargs):
    try:
        Like.objects.filter(
            owner=request.user,
            pin=Pin.objects.get(pk=kwargs['pk']),
        ).delete()
    except:
        return Response(data={'message': 'bad request'},status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

