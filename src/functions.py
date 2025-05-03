import requests

main_url = 'https://v6.exchangerate-api.com/v6/f4e8c67eceb138c32b1fa586/latest/{}'

def get_exchange_rate(base_currency, target_currency):
    url = main_url.format(base_currency)
    response = requests.get(url)
    target_value = response.json()['conversion_rates'][target_currency]
    return target_value
    
def convert_currency(currency, mount):
    url = main_url.format(currency)
    response = requests.get(url)
    target_value = response.json()['conversion_rates']['USD']
    finall_value = target_value * mount
    return finall_value
