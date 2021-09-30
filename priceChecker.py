import bs4, pickle, time
import requests as r

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \
    WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
HEADERS2 = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; \
    Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
FILE = './prices.tsv'

def amazon_price(link):
    print(f"Visitinig {link}")
    res = r.get(link, headers=HEADERS)
    res.raise_for_status()
    PRICE_TAGS = {"priceblock_ourprice", "priceblock_dealprice"}
    for t in PRICE_TAGS:
        obj = bs4.BeautifulSoup(res.text, 'html.parser')
        price = obj.select("#"+t)
        print(price)
        if price:
            return price[0].text

def flipkart_price(link):
    print(f"Visitinig {link}")
    res = r.get(link, headers=HEADERS)
    res.raise_for_status()
    obj = bs4.BeautifulSoup(res.text, 'html.parser')
    # price = obj.select("div._30jeq3._16Jk6d")
    price = obj.select("._16Jk6d")
    print(price)
    if price:
        return price[0].text

# testcases
def test_amazon_price():
    amazon_link = "https://www.amazon.in/HP-24-df0215in-23-8-Inch-Built-3-3250U/dp/B08JM3ZLHF"
    assert amazon_price(amazon_link) is not None

def test_flipkart_price():
    flipkart_link = "https://www.flipkart.com/infinix-hot-10s-heart-ocean-64-gb/p/itma5269c82af950"
    assert flipkart_price(flipkart_link) is not None

if __name__ == '__main__':
    flipkart_link = "https://www.flipkart.com/infinix-hot-10s-heart-ocean-64-gb/p/itma5269c82af950"
    price = flipkart_price(flipkart_link)
    now = time.asctime()
    with open(FILE, 'a') as f:
        f.write(f"{now}\t{price}\n")
        f.close()
