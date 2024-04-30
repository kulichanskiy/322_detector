import requests
from bs4 import BeautifulSoup
from time import sleep

# #headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     "Referer": "https://stawkibet.io/ru/e-sports/esl-pro-league-7523620fe3a94815bf69c92cad317102/prematch",
#     "Sec-Ch-Ua": "\"Opera GX\";v=\"109\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": "\"Windows\"",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "cross-site",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
#     "X-Amzn-Trace-Id": "Root=1-662f306f-192cbde54b6b9deb6c4bddd7"
#   }

url = "https://stawkibet.io/ru/e-sports/esl-pro-league-7523620fe3a94815bf69c92cad317102/prematch"

response = requests.get(url)   
soup = BeautifulSoup(response.text, "lxml") 

with open("pm.html", "w", encoding="utf-8") as f:
    f.write(str(response.text))