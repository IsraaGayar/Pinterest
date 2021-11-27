from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from accounts.models import User
from accounts.permissions import MyUser
from accounts.api.seriallizers import AccountSerializer,ProfileSerializer,UserListSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserProfile(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes=[MyUser]

class UserFollowers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
        except:
            return Response(data={'message': 'No such user'}, status=status.HTTP_400_BAD_REQUEST)
        return user.follower.all()

class UserFollowings(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
        except:
            return Response(data={'message': 'No such user'}, status=status.HTTP_400_BAD_REQUEST)
        return user.following.all()

class AccountCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes=[]



@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow(request,*args,**kwargs):
    try:
        request.user.follower.add(User.objects.get(pk=kwargs['pk']))
    except:
        return Response(data={'message': 'No such user exists'},status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow(request,*args,**kwargs):
    try:
        request.user.follower.remove(User.objects.get(pk=kwargs['pk']))
    except:
        return Response(data={'message': 'your user isnt authonticated'},status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

