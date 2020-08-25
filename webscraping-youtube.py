from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser

busca = input("Insira o nome da música a ser buscada: ")

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=" + busca.strip().replace(' ', '+'))

user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
titulos = []
links = []
for i in user_data:
    titulos.append(i.get_attribute('title'))
    links.append(i.get_attribute('href'))

print(len(links))
print(titulos[:5])
driver.get(links[0])
# webbrowser.open_new_tab(links[0])

