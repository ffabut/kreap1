## program počítá docházky studentek a studentů

lide = {
    "Jana": 0,
    "Daniel": 0,
    "Kamila": 0,
    "Daniela": 0,
    "Jan": 0,
    "Kamil": 0
} # slovnik obsahujici dvojice jmeno-studentky:pocet-dochazek

while True: #nekonecny cyklus - blok se bude neustale opakovat
    jmeno = input("Zadejte jmeno prichozi(ho), pozor musíte být přesní: ")
    lide[jmeno] = lide[jmeno] + 1 # hodnotu uloženou pod klíčem jména zvětšíme o jedna a uložíme zpět pod klíč
    # pokud se uživatelka překlikla, pak dojde k chybě - program nemůže získat hodnotu zpod neexistujícího klíče

    print("Stav dochazky je: ", lide, "\n") #na konci vypiseme soucasny stav dochazky
