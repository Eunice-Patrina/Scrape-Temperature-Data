import requests
import selectorlib
from datetime import datetime

url="http://programmer100.pythonanywhere.com"

def scrapper(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def write(message):
    with open("data.txt", 'a') as file:
        file.write(f'{message}\n')

if __name__ == "__main__":
    date = datetime.now()
    source = scrapper(url)
    value = extract(source)
    write(f'{date.strftime("%Y-%m-%d-%H-%M-%S")},{value}')
