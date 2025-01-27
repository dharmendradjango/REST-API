from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('api/books/', views.movie_list, name="movie-list"),
    path('api/books/<int:pk>', views.movie_detail, name='movie-detail'),
    path('stream/',views.stream_list,name="stream-platform"),
    path('stream/<int:pk>',views.stream_detail,name="stream-platform-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
