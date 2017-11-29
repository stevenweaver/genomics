import json

with open('results/opsin.RELAX.json') as json_data:
    d = json.load(json_data)

tested = d["tested"]["0"]

for key, value in tested.items():
    print(key + "," + value)
