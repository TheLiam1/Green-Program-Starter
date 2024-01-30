import requests
import json

r1_times_gesamt = requests.get("https://smard.de/app/chart_data/122/DE/index_day.json")
json.dump(r1_times_gesamt.json(), open("r1_times_gesamt.json", "w"), indent=4)

with open("r1_times_gesamt.json") as file5:
    data6 = json.load(file5)
current_timestamp6 = data6["timestamps"][-1]
