import requests
from bs4 import BeautifulSoup

CITY_NAME = ""

class SathyaMiddleware:
    def __init__(self,response):
        print("Sathya Middleware Constructor")
        self.get_response = response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        print("Sathya Middleware request")
        r = requests.get("https://mylocation.org/")
        bs = BeautifulSoup(r.text, "html.parser")
        res = bs.find_all("td")
        global CITY_NAME
        CITY_NAME = res[11].text
        print(CITY_NAME)
        return response


def my_location():
    return CITY_NAME