# r1_r2_list = [r1.json(), r2.json()]
# json.dump(r1_r2_list, open("r1_r2_list.json", "w"), indent=4)

import requests
from datetime import datetime as dt
import json

numb = 2
curr_time = dt.now()

"""
Hier werden die Daten angefragt, die die Timestamps für die prognostizierte Erzeugung
von Wind und Photovoltaik liefern.
"""

r1 = requests.get('https://smard.de/app/chart_data/5097/DE/index_quarterhour.json')

"""
Der neueste Timestamp wird dann in eine Variable gespeichert
"""
with open("r1.json") as file:
    data = json.load(file)
right_time_stamp = data["timestamps"][-1]

"""
Hier werden dann erst die Daten abgerufen, wann wie viel Wind und Photovoltaik erzeugt wird.
Dafür wird als Timestamp die Variable genutzt, die wird vorher definiert haben.
"""

r2 = requests.get(f'https://smard.de/app/chart_data/5097/DE/5097_DE_hour_{right_time_stamp}.json')

"""
Hier werden eigentlich erst die Daten aus den Anfragen in zwei Dateien gespeichert.
Ich kann das halt erst hier öffnen, weil die r2 Anfrage unter dem Befehl stehen muss,
wo ich die erste Datei öffne.
Dort wird nämlich die Variable definiert, die in r2 benutzt wird.
Das muss ich auf jeden Fall nochmal verbessern, sieht ziemlich sinnbefreit aus.
Tschau
"""
json.dump(r1.json(), open("r1.json", "w"), indent=4)
json.dump(r2.json(), open("r2.json", "w"), indent=4)

with open("r2.json") as file2:
    data2 = json.load(file2)

print("Current Timestamp")
print(int(curr_time.timestamp()))
