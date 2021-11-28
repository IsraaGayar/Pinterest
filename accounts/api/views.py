from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, filters, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.models import User
from accounts.permissions import MyUser
from accounts.api.seriallizers import AccountSerializer,ProfileSerializer,UserListSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['username', 'first_name','last_name']


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
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['username', 'first_name','last_name']

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
        except:
            return Response(data={'message': 'No such user'}, status=status.HTTP_400_BAD_REQUEST)
        return user.follower.all()

class UserFollowings(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['username', 'first_name', 'last_name']

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

class Followuser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args,**kwargs):
        try:
            following=self.get_object() #the person am gonna follow
        except:
            return Response(data={'message': 'No such a user '}, status=status.HTTP_400_BAD_REQUEST)
        if following in request.user.follower.all():
            return Response(data={'message': 'you already follow that user'},status=status.HTTP_400_BAD_REQUEST)
        else:
            request.user.follower.add(following)
            return Response(data=str(list(request.user.follower.all())),status=status.HTTP_201_CREATED)

class UnFollowuser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args,**kwargs):
        try:
            following=self.get_object() #the person am gonna follow
        except:
            return Response(data={'message': 'No such a user '}, status=status.HTTP_400_BAD_REQUEST)
        if following in request.user.follower.all():
            request.user.follower.remove(following)
            return Response(data=str(list(request.user.follower.all())), status=status.HTTP_201_CREATED)
        else:
          return Response(data={'message': 'you already not following that user'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def Logout(request):
    myuser=request.user
    Token.objects.get(user=myuser).delete()
    Token.objects.create(user=myuser)
    return Response(data={'message': 'you are logged out'}, status=status.HTTP_200_OK)
