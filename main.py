import requests
import selectorlib
from datetime import datetime
import sqlite3

url="http://programmer100.pythonanywhere.com"
connection = sqlite3.connect("data.db")
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

def write_db(date, temperature):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?, ?)",(date, temperature))
    connection.commit()

if __name__ == "__main__":
    date = datetime.now()
    source = scrapper(url)
    value = extract(source)
    write_db(date.strftime("%Y-%m-%d-%H-%M-%S"), value)
