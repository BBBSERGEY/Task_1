
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

def get_course(id):
    return xml.find('Valute', {'ID': id}).Value.text


url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

today = datetime.today()

today = today.strftime('%d/%m/%Y')

payload = {'date_req': today}
response = requests.get(url, params=payload)
xml = bs(response.content, features='xml')