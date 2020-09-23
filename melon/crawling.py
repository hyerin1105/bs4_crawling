import requests
from bs4 import BeautifulSoup

def melon_crawling():
    iamhuman = {
        "User-Agent": "ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    } # useragent를 딕셔너리 형식으로 넣음.

    URL = "https://www.melon.com/chart/day/index.htm"
    result = requests.get(URL, headers=iamhuman)
    soup = BeautifulSoup(result.text, "html.parser")

    """ 순위 """
    rank = soup.find_all("span", {"class": "rank"})
    ranks = []
    for i in rank[1:]: # 순위 타이틀 제거
        ranks.append(i.text)

    """ 노래 제목 """
    name = soup.find_all("div", {"class": "ellipsis rank01"}) # 차트의 곡 요소의 클래스
    names = []
    for i in name:
        names.append(i.find("a").text) # 차트 내용 텍스트로 출력

    """ 가수 """
    singer = soup.find_all("div", {"class": "ellipsis rank02"})
    singers= []
    for i in singer:
        singers.append(i.find("a").text)

    """ 앨범명 """
    album = soup.find_all("div", {"class": "ellipsis rank03"})
    albums = []
    for i in album:
        albums.append(i.find("a").text)

    # for i in range(len(names)):
    #     print(ranks[i], names[i], singers[i], albums[i])

    song_list = list(zip(ranks, names, singers, albums)) #zip으로 묶고 리스트로 생성
    # print(song_list[0])
    return song_list