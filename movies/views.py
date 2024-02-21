from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .models import Actor
from .serializers import MovieSerializer
from .serializers import ActorSerializer

@api_view(['GET', 'POST'])  # GET: 함수형 뷰인 movie_list가 GET 메소드만 허용하는 API를 제공
                                # POST: 생성  요청도 받을 수 있게 POST를 추가
                    # @로 시작하는 부분은 데코레이터 함수, 기존 함수 수정하지 않고 로직 추가하고 싶을때 사용
def movie_list(request):
    if  request.method ==  'GET':
        movies = Movie.objects.all()    # 모든 영화의 객체를 가져옴
        serializer = MovieSerializer(movies, many=True)     # 파이썬 객체 형태인 데이터가 파이썬 딕셔너리 형태로 바뀜
        return Response(serializer.data, status=status.HTTP_200_OK)    # 변환된 데이터는 serializer.data로 접근 가능
    elif request.method == 'POST':
        data = request.data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
# Create your views here.

@api_view(['GET', 'POST'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        serializer = ActorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)