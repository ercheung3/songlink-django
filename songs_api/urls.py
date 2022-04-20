from django.urls import path
from . import views

urlpatterns = [
    # api/lyrics will route to LyricsList view for handling
    path('', views.SongList.as_view(), name='song_list'),
    # api/contacts will route to LyricsDetail view for handling
    path('<int:pk>',views.SongDetail.as_view(), name='song_detail')
]