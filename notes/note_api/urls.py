from django.urls import path
from django.contrib.auth import views as auth_views

from .views import NoteList,NoteCreate,NoteDetail

urlpatterns = [
    path('',NoteList.as_view(),name="note_list"),
    path('create/',NoteCreate.as_view(),
         name='note_create'),
    path('detail/<int:pk>/',NoteDetail.as_view(),name='note_detail'),

  
]