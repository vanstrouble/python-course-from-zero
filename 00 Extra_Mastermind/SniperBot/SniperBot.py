from time import sleep

from requests_html import HTMLSession, AsyncHTMLSession

url = "https://www.amazon.com.mx/dp/B08H6SBB2R/?coliid=I3MPS37E9F656G&colid=2UFB0PGPL00WB&psc=0&ref_=lv_ov_lig_dp_it"

sesion = HTMLSession()

while True:
    r = sesion.get(url)

    buy_zone = r.html.find("btnsWishAddBuy")
    if len(buy_zone) > 0:
        print("Hay Stock!!")
    else:
        print("No hay stock :c")
    sleep(30)
