from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link ="https://glavsnab.com/"
browzer = webdriver.Chrome()
browzer.get(link)

serch_string = browzer.find_element(By.CSS_SELECTOR, "input[id*=top-title-search-input]")
serch_string.send_keys("Инструмент")
cnopka = browzer.find_element(By.CSS_SELECTOR, "button[button*="submit">Найти</button]").click()
time.sleep(2)
proverka = browzer.find_element(By.CSS_SELECTOR, "//*[@id="navigation"]/div/ul/li[3]").text
proverka1 = "Инструмент"
if proverka == proverka1:
    print("Тест прошел успешно")
else:
    print("Тест проверку не прошел")
browzer.quit()