"""
Tento program stahuje vsechny obrazky ze zadane webove adresy.
"""

import requests
from bs4 import BeautifulSoup


server = "https://midi.cz" # url z niz stahovat obrazky
stranka = "/" # chceme stahnout index page, hlavni stranku
url = server + stranka

r = requests.get(url) # stazeni HTML dokumentu
soup = BeautifulSoup(r.text, 'html.parser') # parsovani HTML pomoci BS4
images = soup.find_all('img') # hledani vsech img tagů

x = 1
for image in images:
    src = image.get("src") # ziskani src atributu - adresa obrazku
    # src muze mit 3 podoby:
    # /image.jpg - relativni cesta
    # //server.cz/image.jpg - absolutni cesta s promenlivym protokolem http nebo https dle konkretniho pripojeni
    # http://server.cz/image.jpg - absolutni cesta s pevne danym protokolem
    if src.startswith("http"):
        pass
    elif src.startswith("//"):
        src = "https:" + src # requests potrebuji protokol v adrese, proto jej pridame
    else: #aka relativni cesta - musime pridat protokol a adresu serveru
        src = server + src

    download = requests.get(src) # stazeni obrazku, selze, pokud src neni cela cesta jako "http://server.domena/obrazek.jpg"
    if download.status_code != 200:
        break
    image = download.content
    soubor = open(str(x)+".jpg", "wb") # otevreni souboru pro bajtovy zapis (WB - write byte)
    soubor.write(image) #zapis

    print(x, src)
    x += 1

print("all images has been downloaded")
