from django.urls import path
from . import views

urlpatterns = [
    # api/lyrics will route to LyricsList view for handling
    path('api/lyrics', views.LyricsList.as_view(), name='lyrics_list'),
    #
    path('api/lyrics/<int:pk>',views.LyricsDetail.as_view(), name='lyrics_detail')
]