import module_gesamt as mg
import module_times_gesamt as mtg

right_time = mtg.give_right_timestamp()

data = mg.get_data_out_of_r1_gesamt_json(right_time)

liste = data["series"]
counter = 0
gesamt_liste = []
fertige_werte_Erzeugung = []

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

neueste_MWh_gesamt_777 = fertige_werte_Erzeugung[-72]

counter2 = 0

for wert in gesamt_liste:
    counter2 += 1
    if counter2 % 2 == 0:
        if wert is None:
            finish_counter3 = counter2
            right_timestamp5 = gesamt_liste[finish_counter3 - 146]
            print(f"{right_timestamp5} /Timestamp")
            break

right_timestamp_8458 = right_timestamp5
