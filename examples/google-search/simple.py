"""
Program vypise vysledky Google searche pro zadane slovo.
Nepouziva ale oficialni Google API, ktere ma denni limit hledani.
Namisto toho jen upravuje URL normalniho searche a z HTML vysledku dostava potrebne info.
Defacto se program tvari jako browser.
"""

import requests
from bs4 import BeautifulSoup

search = input("Co chcete najit? ")
# url ziskane po zadani nejakeho dotazu do googlu
# query parametr q oznacuje hledane slovo, to nahradime za HLEDANESLOVO - budeme jej pozdeji nahrazovat
url = "https://www.google.com/search?q=HLEDANESLOVO&source=lnms&sa=X&ved=0ahUKEwjllZC5pZfmAhUKPFAKHabOAjQQ_AUIDSgA&biw=1920&bih=1089&dpr=1"

url = url.replace("HLEDANESLOVO", search) #nahrazeni za fakticky hledane slovo

#falesne headery HTML requestu, aby dotaz vypadal jako z bezneho prohlizece
#vlastni user-agent retezec muzete zjistit na: https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending
fake = {"user-agent":"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}

# klasicke .get(), ale nove s argumentem headers, kterym predavame vlastni headery
response = requests.get(url, headers=fake)

soup = BeautifulSoup(response.text, features="html.parser")

nadpisy = soup.find_all("h3") # hledame vsechny H3 nadpisy

for nadpis in nadpisy:
  print(nadpis.text) #z tagu H3 vypiseme jeho text
