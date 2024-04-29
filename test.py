import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "MatchFilter={%22active%22:false%2C%22live%22:false%2C%22stars%22:1%2C%22lan%22:false%2C%22teams%22:[]}; CookieConsent={stamp:%27w8Ikvkr/nK/lfUFON2aUXO+heLTKCwk7BaQpOr5uQPqMlhnO2V0qrg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1712505064559%2Cregion:%27ua%27}; _ga=GA1.1.1482335603.1712505064; cf_clearance=n9CfQjU58jp50Q2dKniKkFtgKee.enfGgIm1mvzkY_0-1714237412-1.0.1.1-U5a08tZhZb.U5WE49cyvYIApK9BtWYo0V9z.nwYf.ApKGcFMeaElwkweavXus3ybBZG9njomMDUYzBgjHtSpbg; SLG_G_WPT_TO=ru; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; __cf_bm=J5_MbYvyfZHqBzGq2sRCAumpI8EJGNQkKz6OHvRa9YQ-1714368435-1.0.1.1-hXq4vuOJ_fIDAMwEeYyemWmmzB6mpQcaRwHkQh3u25G93mOYKAbXTtCpxxekJxLwKFAPKDdjAEDWD..p4VFMlQ; _ga_525WEYQTV9=GS1.1.1714368435.12.1.1714368458.0.0.0",
    "Referer": "https://www.hltv.org/stats/players/individual/19270/k4sl",
    "Sec-Ch-Ua": "\"Opera GX\";v=\"109\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "X-Amzn-Trace-Id": "Root=1-662f306f-192cbde54b6b9deb6c4bddd7"
  }


url = "https://www.hltv.org/stats/players/19270/k4sl"
sleep(3)
response = requests.get(url, headers=headers)
response.encoding = 'utf8'  
#data = soup.find("div", class_="col stats-rows standard-box")

#name = data.find("div").text


print(htmlString + '\n')