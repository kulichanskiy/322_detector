import requests 
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "theme=dark; SLG_G_WPT_TO=ru; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; __zzatgib-w-bb=MDA0dBA=Fz2+aQ==; _ym_uid=1714328519985994464; _ym_d=1714328519; _ym_isad=2; supportOnlineTalkID=8Uwy70btuODxi2ov4z6lZ8yDnQrXkJmF; _gid=GA1.2.560933413.1714328556; support_chat_code=200; _ga_V52ZRVWFJ6=GS1.1.1714381707.5.0.1714381707.60.0.0; _ga_W36G937MYS=GS1.1.1714381707.5.0.1714381707.60.0.0; _ga=GA1.2.602933309.1714328498; _gat_UA-93149539-8=1; _gat_UA-93149539-1=1; _ym_visorc=b; cfidsgib-w-bb=w0mjNBlwwsKyx1jtcootGI/ln4rogOqf3tIJY0OLZTH8mACppU3L1pqc3SqPKF0/dQms54lZnNa8KC8Ep1onJZOl0hHV4/kQiGsqEhjBNdNlCXCx3lUtt1hwcyLMpB0sw1YRCRlIlDwqkvTt/xNYXEqkOWEYpVF6OvG4gw==; cfidsgib-w-bb=w0mjNBlwwsKyx1jtcootGI/ln4rogOqf3tIJY0OLZTH8mACppU3L1pqc3SqPKF0/dQms54lZnNa8KC8Ep1onJZOl0hHV4/kQiGsqEhjBNdNlCXCx3lUtt1hwcyLMpB0sw1YRCRlIlDwqkvTt/xNYXEqkOWEYpVF6OvG4gw==",
    "Referer": "https://betboom.ru/",
    "Sec-Ch-Ua": "\"Opera GX\";v=\"109\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "X-Amzn-Trace-Id": "Root=1-662f306f-192cbde54b6b9deb6c4bddd7"
  }

url = "https://bifrost.oddin.gg/?referer=https%3A%2F%2Fbetboom.ru%2Fesport&lang=ru&currency=RUB&token=&brandToken=b94ac61d-b060-4892-8242-923bf2303a38&supportedOddsFormats=empty&darkMode=true&q=1714408711252"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

tournament = soup.find("div", class_="BaseLayout__BaseLayoutContainer-sc-9xrm6q-0 eCvRsX")
print(tournament)

# def main (base_url):
#   s = Session()
#   s.headers.update(headers)
#   response = s.get(base_url)
#   soup = (response.text, 'lxml')

#   with open('bb.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)


# main(base_url) 