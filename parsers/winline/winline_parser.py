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


def get_tournament(soup):
    tournament_data = soup.find_all("div", class_="block-sport__champ-item ng-star-inserted")
    with open("1.txt", "a", encoding="utf-8") as f:
        for i in tournament_data:
            tournament_name = i.find('span', class_='block-tournament-header__title')
            f.write(tournament_name.text.strip() + '\n')





# team_data = i.find_all('div', class_='name ng-star-inserted')
#             for j in team_data:
#                 team = j
                
#                 #team_coef_2 = tournament_data.find('div', class_='coefficient-button coefficient-button_fill coefficient-button_align_space-b coefficient-button_generic2 coefficient-button_align_center ng-star-inserted coefficient-button_down')
#                 f.write(j.text.strip() + '\n')
#             f.write('\n')
            

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
    get_tournament(soup)
