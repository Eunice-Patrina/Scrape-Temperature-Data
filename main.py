import requests
import selectorlib

url="http://programmer100.pythonanywhere.com"

def scrapper(url):
    response = requests.get(url)
    source = response.text
    return source


if __name__ == "__main__":
    source = scrapper(url)
    print(source)