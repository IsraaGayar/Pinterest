from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from . import views
app_name='accounts'
urlpatterns = [
    path('profile/list', views.UserList.as_view(),name='userslist'), #checked
    path('profile/<int:pk>', views.UserProfile.as_view(),name='profile'),#checked
    path('profile/<int:pk>/edit', views.AccountDetail.as_view(), name='editaccount'),#checked


    path('profile/<int:pk>/followers', views.UserFollowers.as_view(), name='userfollowers'), #checked
    path('profile/<int:pk>/followings', views.UserFollowings.as_view(), name='userfollowings'), #checked

    path('register', views.AccountCreate.as_view(), name='createuser'), #errors !!
    path('login', obtain_auth_token), #checked


    path('profile/<int:pk>/follow', views.Followuser.as_view({'patch': 'update'}), name='follow'),
    path('profile/<int:pk>/unfollow', views.UnFollowuser.as_view({'patch': 'update'}), name='unfollow'),

]
