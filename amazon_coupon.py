import string
import requests
from smtplib import SMTP
from bs4 import BeautifulSoup as bs
import json
import pymessenger



#URL = 'https://www.amazon.com/Creality-Ender-Max-Neo-Automatic/dp/B0B56FZK3B?th=1'
URL = 'https://www.amazon.com/Writing-Tablet-Drawing-Colorful-Screen/dp/B07THCY3KB/ref=sr_1_8?crid=MMSS5ZX9A3NZ&keywords=limited%2Btime%2Bdeals&qid=1667579143&qu=eyJxc2MiOiI4LjkxIiwicXNhIjoiOC4xOSIsInFzcCI6IjYuOTcifQ%3D%3D&sprefix=limited%2Btime%2Bdeals%2Caps%2C94&sr=8-8&th=1'


headerss = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'From': 'gabriel10@gmail.com'  # This is another valid field
}
page = requests.get(URL ,headers=headerss)
soup = bs(page.content,"html.parser")

try:
    span = soup.find("span", {"class": 'a-price-whole'})
    price = span.text
    print("Price:", price[0:5])
    
except AttributeError:
    price = "No price at the moment"
    print(price)
    
try:
    span2 = soup.find(lambda tag:tag.name=="label" and "Apply" in tag.text)
    coupon = span2.text
    
    print("Coupon:",coupon[1:17])
    
except AttributeError:
    coupon = "No coupon at the moment"
    print(coupon)
    
try:
    span3 = str(soup.find("td", {"class": 'a-span12 a-color-price a-size-base'}))
    for times in range(0,10):
        if span3 == "None":
            page = requests.get(URL ,headers=headerss)
            soup = bs(page.content,"html.parser")
            span3 = str(soup.find("td", {"class": 'a-span12 a-color-price a-size-base'}))
            print("Unable to get Save discount data")
        else:
            break
    print("Save discount data retrieved:", span3[249:252])
    
except AttributeError:
    save = "No save at the moment"
    print(save)