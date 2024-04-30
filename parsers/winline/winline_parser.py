from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs

def get_html_content(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Запускаем Chrome в режиме headless (без отображения GUI)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    # Добавляем задержку до 10 секунд, чтобы дождаться загрузки страницы
    wait = WebDriverWait(driver, 7)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "block-sport__champ-list")))
    html_content = driver.page_source
    driver.quit()
    return html_content

# soup = bs(html_content, 'lxml')

urls = [
    "https://winline.ru/stavki/sport/kibersport/counter-strike",
    "https://winline.ru/stavki/sport/kibersport/dota_2",
    "https://winline.ru/stavki/sport/kibersport/valorant",
    "https://winline.ru/stavki/sport/kibersport/league_of_legends",
    "https://winline.ru/stavki/sport/kibersport/rainbow_six"
]

for url in urls:
    html_content = get_html_content(url)
    soup = bs(html_content, 'lxml')
    filename = url.replace("https://winline.ru/stavki/sport/kibersport/", "") + ".html"
    with open(filename, "w", encoding="utf-8") as f:
     f.write(soup.prettify())





    


