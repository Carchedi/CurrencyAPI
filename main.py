import requests
import json

def curr_value(currency):
    req = 'https://api.exchangerate-api.com/v4/latest/'+currency
    response_API = requests.get(req)
    data = response_API.text
    num = json.loads(data)
    return ("{:.2f}".format(num['rates']['BRL'])) 

print ("Dolar: "+curr_value('USD'))
print ("Euro: "+curr_value('EUR'))
 