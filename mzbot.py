# -*- coding: utf-8 -*-
import atexit
import time
import gdax
import telepot
from telepot.loop import MessageLoop
from Printer import Printer

version = '0.1'
console = Printer(version)
res_info = '*Bitcoin-mzbot*\nI am Matteo Zoia, Computer Sci student at University in Milan.'
res_list = '/list showing command\n/btcusd BTC-USD exchange\n/etheur ETH-EUR exchange\n/etheurstats ETH-EUR full stats'

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    res = (public_client.get_product_ticker(product_id='ETH-EUR'))
    etheur_price = float(res[u'price'])
    res = (public_client.get_product_ticker(product_id='BTC-USD'))
    btcusd_price = float(res[u'price'])
    res = public_client.get_product_24hr_stats('ETH-EUR')
    etheur_24high = float(res[u'high'])
    etheur_24low = float(res[u'low'])
    hl_gap = 100 - (etheur_24low / etheur_24high * 100)
    price_gap = 100 - (etheur_price / etheur_24high * 100)

    etheur_full = '*ETH-EUR*\nExchange: {0:.2f}\nHighest 24h: {1:.2f}\nLowest 24h: {2:.2f}\nH/L gap: {3:.2f}\n_mzbot (data from: gdax)_'.format(etheur_price,etheur_24high,etheur_24low,hl_gap)

    if command == '/info':
        bot.sendMessage(chat_id, res_info, parse_mode='markdown')
    elif command == '/etheur':
        bot.sendMessage(chat_id, '*ETH-EUR*: {0} \n_mzbot (data from: gdax)_'.format(etheur_price), parse_mode='markdown')
    elif command == '/btcusd':
        bot.sendMessage(chat_id, '*BTC-USD*: {0} \n_mzbot (data from: gdax)_'.format(btcusd_price), parse_mode='markdown')
    elif command == '/etheurstats':
        bot.sendMessage(chat_id, etheur_full, parse_mode='markdown')
    elif command == '/list':
        bot.sendMessage(chat_id, res_list)

    console.refresh_header(etheur_price, etheur_24low, etheur_24high, hl_gap, price_gap)


def exit_handler():
    console.exit()

atexit.register(exit_handler)
public_client = gdax.PublicClient()
bot = telepot.Bot('381964164:AAFZxU3Kz98ohJXRpmiGCx6WVfUupRmomjg')
bot.message_loop(handle)
while 1:
    time.sleep(2)