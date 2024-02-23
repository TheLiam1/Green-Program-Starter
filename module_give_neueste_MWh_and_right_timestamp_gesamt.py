import module_gesamt as mg
import module_times_gesamt as mtg

"""
class TotalEnergyProduction:
    def __init__(self):
        self.timestamp = mtg.load_timestamps()[-1]
"""
right_time = mtg.give_right_timestamp()

data = mg.get_data_out_of_r1_gesamt_json(right_time)

liste = data["series"]
counter = 0
gesamt_liste = []
fertige_werte_Erzeugung = []
fertige_werte_Erzeugung_timestamp = []

for i in liste:
    for wert in i:
        counter += 1
        gesamt_liste.append(wert)
        if counter % 2 == 0:
            if wert is None:
                pass
            else:
                fertige_werte_Erzeugung.append(wert)
                fertige_werte_Erzeugung_timestamp.append(gesamt_liste[counter - 2])

print(
    f"Das ist die fertige Werte Erzeugung"
    f"ng für die Timestamps aus der Datei r1_gesamt als Li"
    f"ste:{fertige_werte_Erzeugung_timestamp}, und der letzte Wert:"
    f"{fertige_werte_Erzeugung_timestamp[-1]}")


def give_MWh_gesamt_zu_uhrzeit(zahl):
    neueste_MWh_gesamt_777 = fertige_werte_Erzeugung[zahl]
    # -72 für 6 Uhr morgens
    return neueste_MWh_gesamt_777


counter2 = 0

for wert in gesamt_liste:
    counter2 += 1
    if counter2 % 2 == 0:
        if wert is None:
            finish_counter3 = counter2
            right_timestamp5 = gesamt_liste[finish_counter3 - 4]
            # -146 für 6 Uhr morgens
            print(f"{right_timestamp5} /Timestamp")
            break


def give_right_timestamp_zu_uhrzeit():
    right_timestamp_8458 = right_timestamp5
    return right_timestamp_8458
