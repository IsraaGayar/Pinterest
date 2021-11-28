
from rest_framework import response, generics, permissions, status, viewsets
from rest_framework.response import Response

from accounts.models import User
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

class addPinToBoard(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = boardSerializer
    permission_classes=[IsColaboratorOrReadOnly]

    def update(self, request, *args,**kwargs):
        try:
            myboard=self.get_object()
            data=request.data
        except:
            return Response(data={'message': 'No such a board '}, status=status.HTTP_400_BAD_REQUEST)

        try:
            pin_id=data['pin_id']
        except:
            return Response(data={'message': 'please add a pin_id field with the pin id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            pin = Pin.objects.get(id=pin_id)
            print(pin)
        except:
            return Response(data={'message': 'no such pin available'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        if pin in myboard.savedPins.all():
            return Response(data={'message': 'pin already saved in that board'},status=status.HTTP_400_BAD_REQUEST)
        else:

            myboard.savedPins.add(pin)
            myboard.save()
            serializer=boardSerializer(myboard,context={'request': request})
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class removePinToBoard(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = boardSerializer
    permission_classes=[IsColaboratorOrReadOnly]

    def update(self, request, *args,**kwargs):
        try:
            myboard=self.get_object()
            data=request.data
        except:
            return Response(data={'message': 'No such a board '}, status=status.HTTP_400_BAD_REQUEST)

        try:
            pin_id=data['pin_id']
        except:
            return Response(data={'message': 'please add a pin_id field with the pin id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            pin = Pin.objects.get(id=pin_id)
        except:
            return Response(data={'message': 'no such pin available'}, status=status.HTTP_400_BAD_REQUEST)

        if pin in myboard.savedPins.all():
            myboard.savedPins.remove(pin)
            myboard.save()
            serializer = boardSerializer(myboard, context={'request': request})
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'message': 'pin already not in that board'},status=status.HTTP_400_BAD_REQUEST)

class addcollaboratorToBoard(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = boardSerializer
    permission_classes=[IsColaboratorOrReadOnly]

    def update(self, request, *args,**kwargs):
        try:
            myboard=self.get_object()
            data=request.data
        except:
            return Response(data={'message': 'No such a board '}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_id=data['user_id']
        except:
            return Response(data={'message': 'please add a user_id field with the user id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            collaborator = User.objects.get(id=user_id)
        except:
            return Response(data={'message': 'no such user available'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        if collaborator in myboard.collaborator.all():
            return Response(data={'message': 'user is already a collaborator'},status=status.HTTP_400_BAD_REQUEST)
        else:
            myboard.collaborator.add(collaborator)
            myboard.save()
            serializer=boardSerializer(myboard,context={'request': request})
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class removecollaboratorToBoard(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = boardSerializer
    permission_classes=[IsColaboratorOrReadOnly]

    def update(self, request, *args,**kwargs):
        try:
            myboard=self.get_object()
            data=request.data
        except:
            return Response(data={'message': 'No such a board '}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_id=data['user_id']
        except:
            return Response(data={'message': 'please add a user_id field with the user id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            collaborator = User.objects.get(id=user_id)
        except:
            return Response(data={'message': 'no such user available'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        if collaborator in myboard.collaborator.all():
            myboard.collaborator.remove(collaborator)
            myboard.save()
            serializer = boardSerializer(myboard, context={'request': request})
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'message': 'user is not a collaborator'},status=status.HTTP_400_BAD_REQUEST)