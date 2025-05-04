import requests

main_url = 'https://v6.exchangerate-api.com/v6/f4e8c67eceb138c32b1fa586/latest/{}'

def get_exchange_rate(base_currency, target_currency):
    url = main_url.format(base_currency)
    response = requests.get(url)
    exchange_rate = response.json()['conversion_rates'][target_currency]
    return exchange_rate
    
def convert_currency(currency, amount):
    url = main_url.format(currency)
    response = requests.get(url)
    exchange_rate = response.json()['conversion_rates']['USD']
    final_value = exchange_rate * amount
    return final_value
