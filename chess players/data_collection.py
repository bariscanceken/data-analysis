from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os
import csv

base_dir = os.path.dirname(os.path.abspath(__file__))
path_playersdata = os.path.join(base_dir, 'players.txt')

driver = webdriver.Chrome()
driver.maximize_window()
datas = []

for i in range(1, 3954):
    base_url = f"https://www.chess.com/ratings?page={i}"
    driver.get(base_url)
    
    try:
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div[1]/table/tbody")))
        data = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div[1]/table/tbody")
        datas.append(data.text)

        with open(path_playersdata, 'a', encoding="utf-8") as dosya:
            dosya.write(data.text + "\n")

        print(f"Sayfa {i} verisi kaydedildi.")

    except Exception as e:
        print(f"Sayfa {i} verisi alınırken hata oluştu: {e}")
        continue

    time.sleep(2)

with open(path_playersdata, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip() and not line.strip() == "GM" and not line.strip() == "1"]

players = []
k = 0
while k < len(lines):
    if lines[k].startswith("#"):
        rank = lines[k][1:]
        name = lines[k + 1]
        rating1 = lines[k + 2]
        rating2 = lines[k + 3]
        rating3 = lines[k + 4]
        players.append([rank, name, rating1, rating2, rating3])
        k += 5
    else:
        k += 1

with open(path_playersdata, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["rank", "name", "rating1", "rating2", "rating3"])
    writer.writerows(players)
