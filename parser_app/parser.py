import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt


HOST = "https://kinozed.com"
URL = "https://kinozed.com/sci-fi/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='short clearfix with-mask newshort')
    film = []

    for item in items:
        film.append(
            {
                'title': item.find('div', class_='short-text').get_text(),
                'image': HOST + item.find('div', class_="short-img img-box").find('img').get('src')
            }
        )
    return film


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        film = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            film.extend(get_data(html.text))
            return film

    else:
        raise ValueError('Error in parser function')



HOST = "https://jut.su/"
URL = "https://jut.su/anime/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='all_anime')
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('div', class_='aablock').get_text(),
                'image': HOST + item.find('div', class_="all_anime_image").get('style')
            }
        )
    return anime


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            anime.extend(get_data(html.text))
            return anime

    else:
        raise ValueError('Error in parser function')


