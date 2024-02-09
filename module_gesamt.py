import module_times_gesamt as mtg
import requests
import json

current_timestamp7 = mtg.give_right_timestamp()


def get_data_out_of_r1_gesamt_json(current_time):
    r2_gesamt = requests.get(f"https://smard.de/app/chart_data/122/DE/122_DE_quarterhour_{current_time}.json")
    json.dump(r2_gesamt.json(), open("r1_gesamt.json", "w"), indent=4)

    with open("r1_gesamt.json") as file7:
        data8 = json.load(file7)
    return data8
