## program počítá docházky studentek a studentů
## verze: DELUXE

lide = {} #prazdny slovnik

while True: #nekonecny cyklus - blok se bude neustale opakovat
    jmeno = input("Zadejte jmeno prichozi(ho): ")

    if jmeno in lide: #pokud jiz je klic se jmenem ve slovniku
        lide[jmeno] = lide[jmeno] + 1 #pak hodnotu pod klicem zvetsime o jedna
    else: #pokud klic ve slovniku neni - preklik nebo novy clovek
        lide[jmeno] = 1 #pak pod klic ulozime hodnotu 1

    print("Stav dochazky je: ", lide, "\n") #na konci vypiseme soucasny stav dochazky
