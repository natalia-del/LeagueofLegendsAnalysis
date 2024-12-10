from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Uruchomienie przeglądarki
driver = webdriver.Firefox()

# Otwórz stronę League of Legends
url = "https://universe.leagueoflegends.com/pl_PL/champions/"
driver.get(url)

# Poczekaj na załadowanie zawartości (np. 5 sekund)
time.sleep(5)

# Znajdź wszystkie elementy ze zdjęciami bohaterów
champion_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'image_3oOd avatar_3vJT')]")
champion_name = driver.find_elements(By.XPATH, "//div[contains(@class, 'copy_xxN7')]/h1")

if len(champion_elements) != len(champion_name):
    print("Liczba sie nie zgadza!")
    driver.quit()
    exit()

champion_data = []
for name,image in zip(champion_name,champion_elements):
    img_url = image.get_attribute("data-am-url")
    champion_n = name.text.strip()
    champion_data.append({"Name":champion_n, "URLImg": img_url})
driver.quit()

champion_df = pd.DataFrame(champion_data)
champion_df.to_csv("champion_images.csv", index = False)





