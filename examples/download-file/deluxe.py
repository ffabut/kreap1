"""
Program stahne danou stranku a vypise jeji HTML kod do terminalu.
Take vypise status code odpovedi na html dotaz - 200=OK, 404=NotFound atd...
Stahovani je umisteno do try-except-else bloku, takze chyby pri stahovani nezpusobi pad programu.
"""

import requests # requests 

def downloadPage(url):
    """
    Funkce downloadPage() stahne obsah z dane adresy predane v argumentu "url".
    Pokud je vse OK, pak funkce vrati text html odpovedi.
    Pokud dojde k chybe, vrati funkce prazdny retezec.
    """
    try: # zkusime stahnout stranku z URL
        response = requests.get(url)
    except: # pokud dojde k chybe, funkce vrati prazdny retezec - nedojde k zastaveni programu...
        return ""
    else: # pokud k chybe nedojde, vypiseme status_code a text odpovedi
        return response.text

page = downloadPage("https://nic.cz") # volame funkci s argumentem adresy stranky, navratovou hodnotu funkce ukladame do promenne page
print(page)
