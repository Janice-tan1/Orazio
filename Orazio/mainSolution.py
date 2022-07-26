
import requests
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=W677J7965EU3DEBN"
response = requests.get(url)
details = response.json()
for info in details:
    conversion_rate = f"USD1 = SGD{details[info]['5. Exchange Rate']}"

def convertUSDtoSGD(amount)
    for items in info:
        USD = float(info[items]['5. Exchange Rate'])
        return amount*USD
print(conversion_rate)

from pathlib import Path
import csv
from api import convertUSDtoSGD
coh_path = Path.cwd()/"csv_reports"/"cash-on-hand.csv"

list_coh = []
list_day = []
higher = True

with coh_path.open(mode="r",encoding="UTF-8", newline="") as info:
    reader = csv.reader(info)
    next(reader)
    for line in reader:
        list_coh.append(float(line[1]))
        list_day.append(line[0])

    for i in range(1, len(list_coh)):
        if list_coh[i] < list_coh[i-1]:
            print(f"DAY: {list_day[i]}, AMOUNT: SGD{convertUSDtoSGD(list_coh[i])}")
            higher = False
        else:
            continue
    
    if higher == True:
        print(f"CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
