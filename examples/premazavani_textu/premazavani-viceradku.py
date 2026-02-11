### Viceradkove premazavani textu v konzoli
# tiskneme nekolik radku vcetne newlines - v tomto pripade 6
# a potom posouvame kurzor zpet nahoru o 6 radku, abychom mohli vse pretisknout

import time
from datetime import datetime

lines = 6 # pocet radku, ktere tiskneme, a ktere potrebujeme posunout zpet nahoru

while True:
    now = datetime.now()
    
    # tak nejak nahodne generujeme cislo, ktere se pouzije jako ramecek nad a pod casem
    border = str(now.second + now.minute + now.hour // now.year) * 30

    print(f"{border}")
    print(f"Rok:   {now.year}")
    print(f"Měsíc: {now.month}")
    print(f"Den:   {now.day}")
    print(f"Čas:   {now.strftime('%H:%M:%S')}")
    print(f"{border}")

    time.sleep(0.1) # sleep, protoze nemusime tisknout cas 10x za sekundu, a bez sleepu by to bylo trochu glitchy

    # posun kurzoru zpět nahoru o pocet radku - musi odpovidat poctu printu koncicich defaultnim newlinem \n, ktere jsme pouzili
    print("\033[F" * lines, end="") # kod "\033[F" je ANSI escape code pro posun kurzoru nahoru o jeden radek na jeho zacatek vic info na wiki https://en.wikipedia.org/wiki/ANSI_escape_code#Control_Sequence_Introducer_commands
