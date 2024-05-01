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


def get_info(data):
    #Достаём название турнира
    tournament_data = data.find('div', class_='block-tournament-header ng-star-inserted')
    tournament_name = tournament_data.find('span', class_='block-tournament-header__title')
    with open("info.txt", "a", encoding="utf-8") as f:
        f.write(tournament_name.text.strip() + '\n\n')
    #Достаем название команды
    team_data = data.find_all('div', class_='card ng-star-inserted')  # Записываем все матчи
    for i in team_data: #Перебираем все мачти  
        team_names = i.find_all('div', class_='name ng-star-inserted')  #Записываем две команды соперницы
        with open("info.txt", "a", encoding="utf-8") as f:
            for j in team_names:    # Перебираем эти 2 команды
                team = j    # Записываем команду
                f.write(j.text.strip() + '\n')
            f.write('\n')
            # Достаём кэфы
            team_coef_data = i.find_all('div', class_='card__coeffs')   # Записываем две ленты кэфов
            for j in team_coef_data:    # Перебираем их
                coef_data = j.find_all('span')
                for q in coef_data:
                    f.write(q.text + " " * 4) # Записываем
                f.write('\n')
            f.write('\n\n')


urls = [
    "https://winline.ru/stavki/sport/kibersport/counter-strike",
    "https://winline.ru/stavki/sport/kibersport/dota_2",
    "https://winline.ru/stavki/sport/kibersport/valorant",
    "https://winline.ru/stavki/sport/kibersport/league_of_legends",
    "https://winline.ru/stavki/sport/kibersport/rainbow_six",
]

with open('info.txt', 'w'):
    pass

for url in urls:
    html_content = get_html_content(url)
    soup = bs(html_content, "lxml")
    # filename = url.replace("https://winline.ru/stavki/sport/kibersport/", "") + ".html"
    # with open(filename, "w", encoding="utf-8") as f:
    #     f.write(soup.prettify())
    
    list = soup.find_all('div', class_='block-tournament') 
    
    for match in list:
        get_info(match)
