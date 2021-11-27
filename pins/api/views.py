from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from pins.api.seriallizers import PinListSerializer, PinSerializer
from pins.models import Pin
from pins.permissions import IsOwnerOrReadOnly


class PinList(generics.ListAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinListSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags__name', 'title']



class PinCreate(generics.CreateAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes=[IsOwnerOrReadOnly]


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def SavePin(request,*args,**kwargs):
    try:
        request.user.savedPins.add(Pin.objects.get(pk=kwargs['pk']))
    except:
        return Response(data={'message': 'this pin doesnt exist'},status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def UnsavePin(request,*args,**kwargs):
    try:
        request.user.savedPins.remove(Pin.objects.get(pk=kwargs['pk']))
    except:
        return Response(data={'message': 'your user isnt authonticated'},status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)



