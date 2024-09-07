from django.http import HttpResponse, JsonResponse
from .models import WatchList,StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def movie_list(request):
    movie_list=WatchList.objects.all()
    serialized=WatchListSerializer(movie_list,many=True)
    return JsonResponse(serialized.data, safe=False)


def movie_detail(request,pk):
    movie=WatchList.objects.get(pk=pk)
    serialized=WatchListSerializer(movie)
    return JsonResponse(serialized.data)

#Particular= get, put, detlete
#list= get,Post
@api_view(['GET', 'POST'])
def stream_list(request,format=None):
    """
    List all code stream, or create a new streamplateform.
    """
    if request.method=='GET':
        stream_list=StreamPlatform.objects.all()
        serialized=StreamPlatformSerializers(stream_list,many=True)
        return Response(serialized.data)
    
    elif request.method=='POST':
        _data=request.data
        serialized=StreamPlatformSerializers(data=_data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def stream_detail(request,pk , format=None):
    """
    Retrieve, update or delete.
    """
    try:
        stream_platform=StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = StreamPlatformSerializers(stream_platform)
        return Response(serializer.data)

    elif request.method == 'PUT':
        _data=request.data
        serializer = StreamPlatformSerializers(stream_platform, data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
