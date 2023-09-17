from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.routers import SimpleRouter

#from .views import NoteList,NoteCreate,NoteDetail,NoteViewSet
from .views import NoteViewSet,UserViewSet

# urlpatterns = [
#     path('',NoteList.as_view(),name="note_list"),
#     path('create/',NoteCreate.as_view(),
#          name='note_create'),
#     path('<int:pk>/',NoteDetail.as_view(),name='note_detail'),

  
# ]

router = SimpleRouter()

router.register("users",UserViewSet,basename='users')
router.register("", NoteViewSet, basename="posts")
urlpatterns = router.urls