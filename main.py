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

r1_5097 = requests.get('https://smard.de/app/chart_data/5097/DE/index_quarterhour.json')
json.dump(r1_5097.json(), open("r1_5097.json", "w"), indent=4)

"""
Der neueste Timestamp wird dann in eine Variable gespeichert
"""
with open("r1_5097.json") as file:
    data = json.load(file)
right_time_stamp = data["timestamps"][-1]

"""
Hier werden dann erst die Daten abgerufen, wann wie viel Wind und Photovoltaik erzeugt wird.
Dafür wird als Timestamp die Variable genutzt, die wird vorher definiert haben.
"""

r2_5097 = requests.get(f"https://smard.de/app/chart_data/5097/DE/5097_DE_quarterhour_{right_time_stamp}.json")
"""
Hier werden eigentlich erst die Daten aus den Anfragen in zwei Dateien gespeichert.
Ich kann das halt erst hier öffnen, weil die r2 Anfrage unter dem Befehl stehen muss,
wo ich die erste Datei öffne.
Dort wird nämlich die Variable definiert, die in r2 benutzt wird.
Das muss ich auf jeden Fall nochmal verbessern, sieht ziemlich sinnbefreit aus.
Tschau
"""
json.dump(r2_5097.json(), open("r2_5097.json", "w"), indent=4)

with open("r2_5097.json") as file2:
    data2 = json.load(file2)

liste = data2["series"]
fertige_werte_Erzeugung = []
#fertige_werte_timestamp = []

print("Current Timestamp")
print(int(curr_time.timestamp()))
print("Werte aus series")
counter = 0
gesamt_liste = []
finish_counter = 0
finish_counter3 = 0
counter2 = 0
for i in liste:
    pass
    for wert in i:
        counter += 1
        gesamt_liste.append(wert)
        if counter % 2 == 0:
            if wert is None:
                #finish_counter = counter
                #print(finish_counter)
                pass
            else:
                fertige_werte_Erzeugung.append(wert)
        if counter % 2 != 0:
            #finish_counter2 = int((finish_counter - 3) / 2)
            #fertige_werte_timestamp.append(wert)
            pass


neuester_wert_5097 = fertige_werte_Erzeugung[-1]
MWh = "MWh"
right_time_stamp5 = 0
print(neuester_wert_5097, MWh)
#print(fertige_werte_timestamp)
for wert in gesamt_liste:
    counter2 += 1
    if counter2 % 2 == 0:
        if wert is None:
            finish_counter3 = counter2
            right_timestamp5 = gesamt_liste[finish_counter3 - 4]
            print(right_timestamp5)
            break

print(gesamt_liste)
#print(data2["series"][3])
