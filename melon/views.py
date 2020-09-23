from django.shortcuts import render, redirect
from .models import MelonList
from .crawling import melon_crawling

# Create your views here.
def index(request):
    songs = MelonList.objects.all()
    return render(request, "index.html", {"songs": songs})


def crawling(request):
    melon_data_list = melon_crawling() # 만들어둔 함수로 크롤링 결과값 가져옴
    MelonList.objects.all().delete() # 충돌ㄴㄴ를 위해 모델의 기존 데이터 삭제
    for i in range(len(melon_data_list)):# 크롤링 결과값 개수만큼 반복
        MelonList(
            rank=melon_data_list[i][0], # 모델.순위 = 크롤링 결과값 중 i번째 순위값 저장
            name=melon_data_list[i][1], # 모델.이름 =
            singer=melon_data_list[i][2], # 모델.가수 =
            album=melon_data_list[i][3], #모델.앨범 =
        ).save()
    return redirect("index")