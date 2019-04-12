import ccxt
import collections
import requests
from assets import Assets
import json


def get_coincap_slugs():

    url = "https://api.coincap.io/v2/assets"
    data = requests.get(url)
    data = data.json()
    data = data['data']

    coins = {}

    for item in data:
        coins[item['symbol']] = {'id': item['id'], 'name': item['name']}

    sorted_coins = collections.OrderedDict(sorted(coins.items()))
    return sorted_coins


def get_exchange_symbols():

    assets = Assets()
    slugs = get_coincap_slugs()
    exchanges = ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken']

    coins = {}

    # loop through exchanges, grab symbols
    for exchange_str in exchanges:
        if exchange_str == 'binance':
            exchange = ccxt.binance()
        elif exchange_str == 'bitfinex':
            exchange = ccxt.bitfinex()
        elif exchange_str == 'bittrex':
            exchange = ccxt.bittrex()
        elif exchange_str == 'poloniex':
            exchange = ccxt.poloniex()
        elif exchange_str == 'kraken':
            exchange = ccxt.kraken()
        else:
            exchange = None

        if exchange:
            exchange.load_markets()
            for sym in exchange.symbols:
                if '/BTC' in sym:
                    sym = sym.replace('/BTC', '')
                    if sym not in coins:
                        coins[sym] = {'exchanges': [exchange_str]}
                    else:
                        coins[sym]['exchanges'].append(exchange_str)

    # handle felix and coincap assets
    for coin in coins:
        if coin in assets:
            coins[coin]['exchanges'].append('felix')
        if coin in slugs:
            coins[coin]['id'] = slugs[coin]['id']
            coins[coin]['name'] = slugs[coin]['name']
        else:
            coins[coin]['id'] = None
            coins[coin]['name'] = None

    sorted_coins = collections.OrderedDict(sorted(coins.items()))
    return sorted_coins


coins = get_exchange_symbols()
#coins = get_coincap_slugs()

print(json.dumps(coins))

"""
for coin in coins:
    if 'felix' in coins[coin]['exchanges']:
        print(coin)
        print(coins[coin])
"""

