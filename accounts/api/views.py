from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, filters, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from accounts.permissions import MyUser
from accounts.api.seriallizers import AccountSerializer, ProfileSerializer, UserListSerializer, RegisterationSerializer, \
    ProfilePic
from django.contrib.auth import get_user_model
User = get_user_model()


def get_profilePic(user):
    try:
        # image = user.profile_picture.url
        image = user.profile_picture.url

    except:
        image = None  # we will put the default pic, or we will store it in the frontend to prevent reloading
    return image

class AccountCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterationSerializer
    permission_classes=[]

class LoginUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        picture = get_profilePic(user)

        print(picture)
        return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'username': user.username,
                'profile_picture': picture,
            })

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




# class MyAccountDetails(APIView):
#
#     def get_object(self):
#         try:
#             user=self.request.user
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404



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
