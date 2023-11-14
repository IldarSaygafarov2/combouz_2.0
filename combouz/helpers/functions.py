import requests


def format_price(price):
    return f"{price:,d}".replace(',', ' ')


def convert_price(product_price, _format=True):
    api_key = "0a1fb85a88eafb2934c0bae7"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    resp = requests.get(url).json()
    uzs = resp["conversion_rates"]["UZS"]
    if _format:
        return format_price(round(product_price * uzs))
    return round(product_price * uzs)


def get_digits_from_number(number):
    phone = ''.join(list(filter(str.isdigit, number)))
    return f'+{phone}'
