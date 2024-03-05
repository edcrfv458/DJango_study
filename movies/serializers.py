from rest_framework import serializers  # 시리얼라이즈 생성하기 위해 필요
from .models import Movie
from .models import Actor

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # id는 장고 모델이 자동으로 정의해주는 필드
                                    # get 요청을 보낼 때 함께 조회하기 위해 추가
                                # read_only = True: 조회시에만 사용하고 싶을 때 쓰는 옵션
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)   # 모델에 값을 넣어 주면 데이터가 생성
                                        # **은 언패킹: 리스트나 딕셔너리 형태로 감싸져  있는 값을 풀어서 씀 

    def update(self, instance, validated_data):     # instance는 수정할 데이터
        instance.name = validated_data.get('name', instance.name)
        instance.opening_date = validated_data.get('opening_date', instance.opening_date)
        instance.running_time = validated_data.get('running_time', instance.running_time)
        instance.overview = validated_data.get('overview', instance.overview)
        instance.save()
        return instance

class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)