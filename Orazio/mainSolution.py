hello
can yall see
yes can see
hi
import requests
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=W677J7965EU3DEBN"
response = requests.get(url)
details = response.json()
for info in details:
    conversion_rate = f"USD1 = SGD{details[info]['5. Exchange Rate']}"
