from django.urls import path

from comments.api.views import CommentCreate
from . import views

app_name='boards'
urlpatterns = [
    path('list', views.Boardview.as_view(), name='boardlist'),
    path('create', views.Boardview.as_view(), name='boardcreate'),
    path('<int:pk>', views.boardDetail.as_view(), name='boarddetails'),

    path('<int:boardpk>/savepin/<int:pinpk>', views.SavePinInBoard, name='BoardPinSave'),
    path('<int:boardpk>/unsavepin/<int:pinpk>', views.UnSavePinInBoard, name='BoardPinUnSave'),

]