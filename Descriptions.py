import time
from idlelib.iomenu import encoding
from pickle import GLOBAL

import pandas as pd
import requests
import csv
import pandas

class response_error(Exception):
    pass

name_df = pd.read_csv(r"C:\Users\natal\Desktop\LOL zdjecia\pythonProject\champion_images.csv")

name_list = [name.capitalize() for name in name_df["Name"]]
print(name_list)

url = 'https://ddragon.leagueoflegends.com/cdn/14.2.1/data/en_US/champion.json'


respone = requests.get(url)

if respone.status_code == 200:
    data = respone.json() # dane zmianimy na obiekt pythona z JSON
    champ_data = data['data']

    data_list= ["Name","Title","Descriptions"]

    for champ_name in name_list:
        champion_data = champ_data.get(champ_name)
        if champion_data:
            name = champion_data.get('id', 'Unkown name')
            title = champion_data.get('title', 'Unkown title')
            description = champion_data.get('blurb', 'No desc')

            # Wyświetlenie danych w konsoli
            print(f"DESC: {name}: {title} : {description}")

            data_list.append([name,title,description])
        else:
            print(f"Can't find champ {champ_name}")
            data_list.append([champ_name,"No data","No data"])
        time.sleep(1)

    with open("champion_desciprions.csv","w",encoding="UTF-8",newline="") as champ_file:
        csv_object = csv.writer(champ_file) #obiekt , aby zapisać csv
        csv_object.writerows(data_list) #zapisanie wierszy

    print("Dane zostały zapisane")

else:
    raise response_error(f"Błąd w połączeniu {respone.status_code}")

