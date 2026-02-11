### Jednoduche premazavani jednoho radku v konzoli
# skript vykazuje dojem, ze se text animuje na miste
# ve skutecnosti neustale pretiskujeme ten samy jeden radek

import time

i = 0
while True:
    print(
        f"\r{i}",        # jeste nez vytiskneme text, zaciname hned \r pro navrat kurzoru na zacatek radku, abysme nasledne pretiskli, co uz jsme tam meli
        end=200*" ",     # 200 prazdnych znaku, aby se kurzor zobrazoval mimo pozornost uzivatelstva - ale pozor zadny newline \r!
        flush=True       # flush=True pro okamzite zobrazeni textu bez bufferovani, vetsi jistota
        )
    
    i += 1
    time.sleep(0.01) # sleep je optional, ale bez nej kurzor trochu blika a glitchuje, protoze se radek premazava opravdu velmi rychle
