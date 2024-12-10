import time
import pandas as pd
import requests
import csv
import pandas
import unicodedata

class response_error(Exception):
    pass

name_df = pd.read_csv(r"C:\Users\natal\Desktop\LOL zdjecia\pythonProject\champion_images.csv")
name_list = [
    unicodedata.normalize("NFKD", name.replace("'", "").replace("’", "").replace(" ", "")).encode("ascii", "ignore").decode("utf-8").capitalize()
    for name in name_df["Name"]
]
print(name_list)
skin_data = [["Champion", "Skin Name", "Skin ID", "Has Chromas", "Image URL"]]

for name in name_list:
    if name:
        url = f'https://ddragon.leagueoflegends.com/cdn/14.23.1/data/en_US/champion/{name}.json'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json() # dane zmianimy na obiekt pythona z JSON
            champ_skins = data['data'][name]['skins']

            for skin in champ_skins:
                skin_name = skin.get('name', 'Default')
                skin_id = skin.get('id', 'Unkown id')
                has_chromas = skin.get('chromas', False)

                image_url = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{name}_{skin["num"]}.jpg'

                skin_data.append([name,skin_name,skin_id,has_chromas,image_url])
                print(f"Champion: {name}, Skin: {skin_name}")
            time.sleep(3)
        else:
            print(f"Can't find data for {name}. Response: {response.status_code}")
            skin_data.append([name, "No data", "No data", "No data", "No data"])
    else:
        print(f"Can't find champ {name}")
        data_list.append([name, "No data", "No data","No data","No data"])

with open("champion_skins.csv","w",encoding="UTF-8",newline="") as champ_file:
    csv_object = csv.writer(champ_file) #obiekt , aby zapisać csv
    csv_object.writerows(skin_data) #zapisanie wierszy

    print("Dane zostały zapisane")


