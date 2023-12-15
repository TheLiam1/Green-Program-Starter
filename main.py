import requests

r = requests.get('https://smard.api.proxy.bund.dev/app/chart_data/1223/DE/1223_DE_hour_1627250400000.json')
print(r.content)
