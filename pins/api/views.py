from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, filters, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from pins.api.seriallizers import PinListSerializer, PinSerializer
from pins.models import Pin
from pins.permissions import IsOwnerOrReadOnly


class PinList(generics.ListAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinListSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'description', 'tags__name']



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


class savePin(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args,**kwargs):
        try:
            mypin=self.get_object()
            # data=request.data
        except:
            return Response(data={'message': 'No such a pin '}, status=status.HTTP_400_BAD_REQUEST)
        if mypin in request.user.savedPins.all():
            return Response(data={'message': 'pin already saved'},status=status.HTTP_400_BAD_REQUEST)
        else:
            request.user.savedPins.add(mypin)
            return Response(data=str(list(request.user.savedPins.all())),status=status.HTTP_201_CREATED)

class unsavePin(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args,**kwargs):
        try:
            mypin=self.get_object()
            # data=request.data
        except:
            return Response(data={'message': 'No such a board '}, status=status.HTTP_400_BAD_REQUEST)

        if mypin in request.user.savedPins.all():
            request.user.savedPins.remove(mypin)
            return Response(data=str(list(request.user.savedPins.all())), status=status.HTTP_201_CREATED)
        else:
           return Response(data={'message': 'pin is not saved'}, status=status.HTTP_400_BAD_REQUEST)

