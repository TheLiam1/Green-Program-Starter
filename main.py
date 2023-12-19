import requests
from datetime import datetime as dt
numb = 2
curr_time = dt.now()

#for i in range(0, numb):
    #time_stamp_string = str(time_stamp)
r = requests.get('https://smard.de/app/chart_data/1223/DE/1223_DE_hour_1702854000000.json')
print(r.content)
    #numb += 1

print(int(curr_time.timestamp()))
print(curr_time)
