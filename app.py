from db import record_price
from priceChecker import flipkart_price
import time

flipkart_link = "https://www.flipkart.com/infinix-hot-10s-heart-ocean-64-gb/p/itma5269c82af950"
while True:
    price = flipkart_price(flipkart_link)
    now = time.asctime()
    print(f"{now}\t{price}")
    record_price((now, price))
    time.sleep(5*60)
