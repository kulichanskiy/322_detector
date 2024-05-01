import requests
from bs4 import BeautifulSoup as bs

headers = {  #Что бы сайты не детектили
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Cookie": "platform_type=desktop; auid=U5PNIGYv0fo0xkTZA0y5Ag==; is12h=0; lng=en; SLG_G_WPT_TO=ru; SESSION=d0c0d50fb11165223e1f381a32b94251; tzo=3; _glhf=1714427759; che_g=a2119ffd-701c-e4c8-5571-aabfaedf20ba; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; ggru=167; application_locale=en; sh.session.id=c41c7aa6-2640-4836-9900-343dac3df917; che_i=1; cookies_agree_type=3; _gcl_au=1.1.923709018.1714410186; _ga_4MKFXHBFXH=GS1.1.1714410186.1.0.1714410186.0.0.0; _ga=GA1.1.610647392.1714410186; window_width=898"
}

r = requests.get("https://1xbet.com/en/live/esports")
soup = bs(r.content, 'lxml')
data = soup.find("div", class_="ui-dashboard dashboard betting-dashboard__app")

def get_tournament_name():
    tournament_data = data.find_all("a", class_="ui-dashboard-champ-name__label ui-dashboard-champ-name__link")
    for i in tournament_data:
        tournament_name = i.find("span", class_="caption__label")
        yield tournament_name.text.strip()

def get_team_name():
    name_data = data.find("a", class_="dashboard-game-block__link dashboard-game-block-link")
    for i in name_data:
        name1 = i.find("span", class_="caption__label")
        name2 = i.find("span", class_="caption__label")
    print(name1.text.strip() + "\n" + name2.text.strip() + "\n\n")


get_team_name()