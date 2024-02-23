# r1_r2_list = [r1.json(), r2.json()]
# json.dump(r1_r2_list, open("r1_r2_list.json", "w"), indent=4)
import subprocess
from getpass4 import getpass
import requests
from datetime import datetime as dt
import json
import time

import module_give_neueste_MWh_and_right_timestamp_gesamt as Gesamt

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

r2_wind_and_solar = requests.get(
    f"https://smard.de/app/chart_data/5097/DE/5097_DE_quarterhour_{current_timestamp}.json")
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
fertige_werte_erzeugung_timestamp = []
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
                fertige_werte_erzeugung_timestamp.append(gesamt_liste[counter - 2])
neuester_wert_5097 = fertige_werte_Erzeugung[-1]


# -1 wäre hier dann die Erzeugung für 23:45 an diesem Tag


def give_erzeugung_5097_zu_uhrzeit(zahl):
    neuester111_wert_5097 = fertige_werte_Erzeugung[zahl]
    return neuester111_wert_5097


MWh = "/MWh"
right_time_stamp5 = 0
print(neuester_wert_5097, MWh)

counter3 = 0
gesamt_liste2 = []

for i in liste2:
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
            right_timestamp5 = gesamt_liste[finish_counter3 - 4]
            # print(f"{right_timestamp5} /Timestamp")
            break

counter4 = 0


def give_right_timestamp_zu_uhrzeit_gruen():
    return right_timestamp5


# print(gesamt_liste)


# print("Werte aus series aus der Datei r2_sonstige.json:")
# print("------------------------------------------------")
# print("")
# print(f"{neuester_wert_715} /MWh")

for wert2 in gesamt_liste2:
    counter4 += 1
    if counter2 % 2 == 0:
        if wert2 is None:
            finish_counter10 = counter4
            right_timestamp10 = gesamt_liste2[finish_counter10 - 4]
            # print(f"{right_timestamp10} /Timestamp")
            break

print(f"{fertige_werte_erzeugung_timestamp[-1]} /Timestamp")
print(f"{dt.fromtimestamp(fertige_werte_erzeugung_timestamp[-1] // 1000)} /Datetime of the Timestamp")

MWh6 = Gesamt.give_MWh_gesamt_zu_uhrzeit(-1)
Timestamp8 = Gesamt.fertige_werte_Erzeugung_timestamp[-1]
# Wenn alles so bleibt, dann ist minus 144 12 an diesem Tag
date5 = dt.fromtimestamp(Timestamp8 // 1000)
print("")
print("Werte aus der Datei module_give_neueste_MWh_and_right_timestamp_gesamt.py")
print("-------------------------------------------------------------------------")
print(f"{MWh6} /MWh")
print(f"{Timestamp8} /Timestamp")
print(f"{date5} /Datetime of the Timestamp")
print("")
print(Gesamt.fertige_werte_Erzeugung)
print("")
print("")
print("")
print("")
print("")
print("")
print("")

anteile_in_liste = []
nur_anteile = []
nur_nur_anteil = []


def give_anteil_zu_uhrzeit(zahl1_wert):
    counter10 = 0
    while zahl1_wert >= -95:
        gesamtwert_zu_uhrzeit = Gesamt.give_MWh_gesamt_zu_uhrzeit(zahl1_wert)
        # timestamp_zu_uhrzeit_gesamt = mgn.give_right_timestamp_zu_uhrzeit()

        gruener_wert_zu_uhrzeit = fertige_werte_Erzeugung[zahl1_wert]

        anteil_an_gruenem_strom = gruener_wert_zu_uhrzeit / gesamtwert_zu_uhrzeit

        nur_anteile.append(anteil_an_gruenem_strom * 100)

        nur_anteile.append(Gesamt.fertige_werte_Erzeugung_timestamp[zahl1_wert])

        anteile_in_liste.append(anteil_an_gruenem_strom)

        anteile_in_liste.append(Gesamt.fertige_werte_Erzeugung_timestamp[zahl1_wert])

        anteile_in_liste.append(dt.fromtimestamp(fertige_werte_erzeugung_timestamp[zahl1_wert] // 1000))

        anteile_in_liste.append(zahl1_wert)

        zahl1_wert -= 1

    for i in nur_anteile:
        counter10 += 1
        if counter10 % 2 != 0:
            nur_nur_anteil.append(i)

    groesster_anteil_nur_anteile_liste = max(nur_nur_anteil)

    index_groesster_anteil_nur_anteile_liste = nur_nur_anteil.index(groesster_anteil_nur_anteile_liste)

    timestamp_zu_groesster_anteil_nur_anteile_liste = nur_anteile[index_groesster_anteil_nur_anteile_liste * 2 + 1]
    datetime_zu_max_timestamp = dt.fromtimestamp(timestamp_zu_groesster_anteil_nur_anteile_liste // 1000)
    print(anteile_in_liste)
    print(f"Datetime: {datetime_zu_max_timestamp}")
    # 1708079400000
    # 59.99189298743413
    print(f"Timestamp: {timestamp_zu_groesster_anteil_nur_anteile_liste}")

    print(f"Maximaler Wert: {groesster_anteil_nur_anteile_liste} %")

    print(f"Index: {index_groesster_anteil_nur_anteile_liste}")

    dt_object = 1708704965
    return dt_object
    # time = dt_object.strftime('%H:%M')
    # sd.every().day.at(formatted_time).do(führe_program_aus_2())


give_anteil_zu_uhrzeit(-1)


def fuehre_program_aus_2():
    # print("hallo")
    # programm = "open"
    # argumente = ["-a", "notepad.exe"]

    password = getpass('Bitte gib dein Passwort ein: ')

    # Führe den Texteditor mit sudo und dem eingegebenen Passwort aus
    subprocess.run(["sudo", "-S", "/Applications/Pages.app"], input=f"{password}\n".encode("utf-8"))


right_time = 0
stunde = 0
minute = 0
sec = 0
"""
hour = int(input("In welcher Stunde soll die Funktion aufgerufen werden?: "))
minute2 = int(input("In welcher Minute soll die Funktion aufgerufen werden?: "))
sekunde = int(input("In welcher Sekunde soll die Funktion aufgerufen werden?: "))
"""
c = 0

while c == 0:
    unix_zeitstempel = time.time()
    timestamp = time.localtime(unix_zeitstempel)

    if timestamp.tm_hour == 17 and timestamp.tm_min == 38 and timestamp.tm_sec == 0:
        give_anteil_zu_uhrzeit(-1)
        right_time = give_anteil_zu_uhrzeit(-1)
        yes = time.localtime(right_time)
        stunde = yes.tm_hour
        minute = yes.tm_min
        sec = yes.tm_sec

    if timestamp.tm_hour == stunde and timestamp.tm_min == minute and timestamp.tm_sec == sec:
        fuehre_program_aus_2()

# Beispielaufruf
# input_time = '12:34:56'
# output_time = convert_format(input_time)
# print(output_time)

# print(nur_anteile)
# print(nur_nur_anteil)

# print(f"{give_anteil_zu_uhrzeit(-1) * 100} %")


# datetime = give_anteil_zu_uhrzeit(-1)
# dt_object = dt.utcfromtimestamp(datetime)
# sd.every().day.at("01:00").do(give_anteil_zu_uhrzeit, zahl1_wert=-1)
# formatted_time = dt_object.strftime('%H:%M')
# Hier mus ich noch die datetime in das richtige Format formatieren, wenn das so funktioniert
# mit dem Rückgabewert der Datetime, aber ich schätze mal schon
# sd.every().day.at("17:31").do(give_anteil_zu_uhrzeit, zahl1_wert=-1)
# 59.99189298743413
# 1708112700000
# import subprocess

# Beispiel: Öffne den Texteditor auf einem Mac
# programm = "open"
# argumente = ["-a", "Microsoft Word"]
# hier kannst du die Argumente für das Programm anpassen

# Führe das Programm aus
# subprocess.run([programm] + argumente)

# Beispiel: Starten von Notepad unter Windows
# subprocess.run(["notepad.exe"])
