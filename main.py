# r1_r2_list = [r1.json(), r2.json()]
# json.dump(r1_r2_list, open("r1_r2_list.json", "w"), indent=4)

import requests
from datetime import datetime as dt
import json

import module_give_neueste_MWh_and_right_timestamp_gesamt
import module_give_neueste_MWh_and_right_timestamp_gesamt as gesamt


curr_time = dt.now()

"""
Hier werden die Daten angefragt, die die Timestamps für die prognostizierte Erzeugung
von Wind und Photovoltaik liefern.
"""

r1_times_wind_and_solar = requests.get('https://smard.de/app/chart_data/5097/DE/index_quarterhour.json')
json.dump(r1_times_wind_and_solar.json(), open("r1_times_wind_and_solar.json", "w"), indent=4)

"""
Der neueste Timestamp wird dann in eine Variable gespeichert
"""
with open("r1_times_wind_and_solar.json") as file:
    data = json.load(file)
current_timestamp = data["timestamps"][-1]

r1_times_sonstige = requests.get("https://smard.de/app/chart_data/715/DE/index_hour.json")
json.dump(r1_times_sonstige.json(), open("r1_times_sonstige.json", "w"), indent=4)

with open("r1_times_sonstige.json") as file2:
    data3 = json.load(file2)
current_timestamp2 = data3["timestamps"][-1]
"""
Hier werden dann erst die Daten abgerufen, wann wie viel Wind und Photovoltaik erzeugt wird.
Dafür wird als Timestamp die Variable genutzt, die wird vorher definiert haben.
"""


r2_wind_and_solar = requests.get(f"https://smard.de/app/chart_data/5097/DE/5097_DE_quarterhour_{current_timestamp}.json")
"""
Hier werden eigentlich erst die Daten aus den Anfragen in zwei Dateien gespeichert.
Ich kann das halt erst hier öffnen, weil die r2 Anfrage unter dem Befehl stehen muss,
wo ich die erste Datei öffne.
Dort wird nämlich die Variable definiert, die in r2 benutzt wird.
Das muss ich auf jeden Fall nochmal verbessern, sieht ziemlich sinnbefreit aus.
Tschau
"""
json.dump(r2_wind_and_solar.json(), open("r2_wind_and_solar.json", "w"), indent=4)

with open("r2_wind_and_solar.json") as file3:
    data2 = json.load(file3)

r2_sonstige = requests.get(f"https://smard.de/app/chart_data/715/DE/715_DE_hour_{current_timestamp2}.json")

json.dump(r2_sonstige.json(), open("r2_sonstige.json", "w"), indent=4)

with open("r2_sonstige.json") as file4:
    data4 = json.load(file4)

liste = data2["series"]
liste2 = data4["series"]
fertige_werte_Erzeugung = []
fertige_werte_Erzeugung2 = []

print("Current Timestamp:")
print("------------------")
print("")
print(int(curr_time.timestamp()))
print("")
print("Werte aus series aus der Datei r2_wind_and_solar.json:")
print("-----------------")
print("")
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
                pass
            else:
                fertige_werte_Erzeugung.append(wert)

neuester_wert_5097 = fertige_werte_Erzeugung[-72]
MWh = "/MWh"
right_time_stamp5 = 0
print(neuester_wert_5097, MWh)

counter3 = 0
gesamt_liste2 = []

for i in liste2:
    pass
    for wert in i:
        counter3 += 1
        gesamt_liste2.append(wert)
        if counter % 2 == 0:
            if wert is None:
                pass
            else:
                fertige_werte_Erzeugung2.append(wert)

neuester_wert_715 = fertige_werte_Erzeugung2[-1]

for wert in gesamt_liste:
    counter2 += 1
    if counter2 % 2 == 0:
        if wert is None:
            finish_counter3 = counter2
            right_timestamp5 = gesamt_liste[finish_counter3 - 146]
            print(f"{right_timestamp5} /Timestamp")
            break

counter4 = 0

# print(gesamt_liste)
print(f"{dt.fromtimestamp(right_timestamp5 // 1000)} /Datetime of the Timestamp")

#print("Werte aus series aus der Datei r2_sonstige.json:")
#print("------------------------------------------------")
#print("")
#print(f"{neuester_wert_715} /MWh")

for wert2 in gesamt_liste2:
    counter4 += 1
    if counter2 % 2 == 0:
        if wert2 is None:
            finish_counter10 = counter4
            right_timestamp10 = gesamt_liste2[finish_counter10 - 4]
            #print(f"{right_timestamp10} /Timestamp")
            break

#print(f"{dt.fromtimestamp(right_timestamp10 // 1000)} /Datetime of the Timestamp")

MWh6 = gesamt.neueste_MWh_gesamt_777
Timestamp8 = gesamt.right_timestamp_8458
date5 = dt.fromtimestamp(Timestamp8 // 1000)
print("")
print("Werte aus der Datei module_give_neueste_MWh_and_right_timestamp_gesamt.py")
print("-------------------------------------------------------------------------")
print(f"{MWh6} /MWh")
print(f"{Timestamp8} /Timestamp")
print(f"{date5} /Datetime of the Timestamp")
print("")
print(module_give_neueste_MWh_and_right_timestamp_gesamt.fertige_werte_Erzeugung)