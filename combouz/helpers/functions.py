import requests


def convert_price(product_price):
    api_key = "0a1fb85a88eafb2934c0bae7"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    resp = requests.get(url).json()
    uzs = resp["conversion_rates"]["UZS"]
    return round(product_price * uzs)
    


def format_price(price):
    return f"{price:,d}".replace(',', ' ')
