from django.shortcuts import render
from rest_framework import response, generics, permissions, status

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from boards.api.seriallizers import boardSerializer
from boards.models import Board
from boards.permissions import IsColaboratorOrReadOnly
from pins.models import Pin


class Boardview(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = boardSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class boardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = boardSerializer
    permission_classes=[IsColaboratorOrReadOnly]


@api_view(['GET'])
@permission_classes([IsColaboratorOrReadOnly])
def SavePinInBoard(request,*args,**kwargs):
    try:
        myboard=Board.objects.get(pk=kwargs['boardpk'])
    except:
        return Response(data={'message': 'No such a board '},status=status.HTTP_400_BAD_REQUEST)
    try:
        mypin=Pin.objects.get(pk=kwargs['pinpk'])
    except:
        return Response(data={'message': 'No such pin'},status=status.HTTP_400_BAD_REQUEST)

    myboard.savedPins.add(mypin)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsColaboratorOrReadOnly])
def UnSavePinInBoard(request,*args,**kwargs):
    try:
        myboard=Board.objects.get(pk=kwargs['boardpk'])
    except:
        return Response(data={'message': 'No such a board '},status=status.HTTP_400_BAD_REQUEST)
    try:
        mypin=Pin.objects.get(pk=kwargs['pinpk'])
    except:
        return Response(data={'message': 'No such pin'},status=status.HTTP_400_BAD_REQUEST)

    myboard.savedPins.remove(mypin)
    return Response(status=status.HTTP_200_OK)
