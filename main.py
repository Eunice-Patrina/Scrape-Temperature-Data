import requests
import selectorlib

url="http://programmer100.pythonanywhere.com"

def scrapper(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value




if __name__ == "__main__":
    source = scrapper(url)
    value = extract(source)
    print(value)