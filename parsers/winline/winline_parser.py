from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs


def get_html_content(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "--headless"
    )  # Запускаем Chrome в режиме headless (без отображения GUI)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    # Добавляем задержку до 10 секунд, чтобы дождаться загрузки страницы
    wait = WebDriverWait(driver, 7)
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "block-sport__champ-list"))
    )
    html_content = driver.page_source
    driver.quit()
    return html_content


def get_tournament(data):
    tournament_name = data.find('span', class_='block-tournament-header__title')
    with open("1.txt", "a", encoding="utf-8") as f:
        f.write(tournament_name.text.strip() + '\n')


def get_team_name(data):
    team_data = data.find('div', class_='body-left__names name')
    team_names = team_data.find_all('div', class_='name ng-star-inserted')
    with open("1.txt", "a", encoding="utf-8") as f:
        for i in team_names:
            team = i
            f.write(i.text.strip() + '\n')
        f.write('\n')
        #Тут пиздец, пока не придумал как решить
        count = 0
        team_coef_data = data.find_all('div', class_='coefficient-button coefficient-button_fill coefficient-button_align_space-b coefficient-button_generic2 coefficient-button_align_center ng-star-inserted')
        for i in team_coef_data:
            if count != 2:
                f.write(i.text.strip() + " " * 4)
            else:
                f.write('\n' + i.text.strip() + " " * 4)  
# soup = bs(html_content, 'lxml')

urls = [
    "https://winline.ru/stavki/sport/kibersport/counter-strike",
    # "https://winline.ru/stavki/sport/kibersport/dota_2",
    # "https://winline.ru/stavki/sport/kibersport/valorant",
    # "https://winline.ru/stavki/sport/kibersport/league_of_legends",
    # "https://winline.ru/stavki/sport/kibersport/rainbow_six",
]

for url in urls:
    html_content = get_html_content(url)
    soup = bs(html_content, "lxml")
    filename = url.replace("https://winline.ru/stavki/sport/kibersport/", "") + ".html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(soup.prettify())
    
    list = soup.find('div', class_='block-sport__champ-item ng-star-inserted') 
    
    for match in list:
        get_tournament(match)
        get_team_name(match)
        get_team_coef(match)