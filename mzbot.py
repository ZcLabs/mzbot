import atexit
import time
import gdax
from Printer import Printer

version = '0.1'
console = Printer(version)

def exit_handler():
    console.exit()
atexit.register(exit_handler)

# refactor this
public_client = gdax.PublicClient()

while 1:
    res = (public_client.get_product_ticker(product_id='ETH-EUR'))
    etheur_price = float(res[u'price'])
    res = public_client.get_product_24hr_stats('ETH-EUR')
    etheur_24high = float(res[u'high'])
    etheur_24low = float(res[u'low'])
    hl_gap = 100 - (etheur_24low / etheur_24high * 100)
    price_gap = 100 - (etheur_price / etheur_24high * 100)

    console.refresh_header(etheur_price, etheur_24low, etheur_24high, hl_gap, price_gap)
    time.sleep(2)