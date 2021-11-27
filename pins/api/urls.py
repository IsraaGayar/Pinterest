from django.urls import path

from comments.api.views import CommentCreate, LikePin, unLikePin
from . import views

app_name='pins'
urlpatterns = [
    path('list', views.PinList.as_view(),name='pinlist'),#checked
    path('create', views.PinCreate.as_view(), name='pincreate'),#checked
    path('<int:pk>', views.PinDetail.as_view(),name='pindetails'),#checked

    path('<int:pk>/comment', CommentCreate.as_view(), name='CommentCreate'),

    path('<int:pk>/save', views.SavePin, name='pinsave'),#checked
    path('<int:pk>/unsave', views.UnsavePin, name='pinunsave'),#checked

    path('<int:pk>/like/<str:liketype>', LikePin, name='pinlike'),
    path('<int:pk>/unlike', unLikePin, name='pinunlike'),
]