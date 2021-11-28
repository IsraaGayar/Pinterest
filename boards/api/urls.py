from django.urls import path
from . import views

app_name='boards'
urlpatterns = [
    path('list', views.Boardview.as_view(), name='boardlist'),
    path('create', views.Boardview.as_view(), name='boardcreate'),
    path('<int:pk>', views.boardDetail.as_view(), name='boarddetails'),

    path('<int:pk>/savepin', views.addPinToBoard.as_view({'patch': 'update'}), name='BoardPinSave2'),
    path('<int:pk>/unsavepin', views.removePinToBoard.as_view({'patch': 'update'}), name='BoardPinSave2'),

    path('<int:pk>/addcollaborator', views.addcollaboratorToBoard.as_view({'patch': 'update'}), name='BoardCollaSave2'),
    path('<int:pk>/removecollaborator', views.removecollaboratorToBoard.as_view({'patch': 'update'}), name='BoardCollaSave2'),

]