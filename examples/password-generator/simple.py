"""
Program generuje nahodne heslo o delce zadane uzivatelkou.
V programu nepouzivame zadne funkce, vse jde pekne radek po radku...
"""

import random # importujeme modul random

delkaHesla = input("Jak ma byt heslo dlouhe? ") # uzivatelka zada delku hesla
delkaHesla = int(delkaHesla) # ale pozor, vstup je string, takze pomoci funkce int() jej prevedeme na cele cislo integer

heslo = "" # prazdna promenna typu string, do ktere budeme ukladat vygenerovane znaky

for i in range(delkaHesla): # cyklus for se zopakuje tolikrat, jake cislo bylo zadane a je v delkaHesla
    cislo = random.randint(33, 126) # funkce generuje nahodne cislo mezi 33 a 126 - ty predstavuji celkem pekne znaky (pismena,tecky,zavorky atd...)
    znak = chr(cislo) # funkce chr() prevadi cisla na znaky, ktere jim odpovidaji
    heslo = heslo + znak # do promenne heslo ulozime to, co v ni je a nakonec pridame nove vygenerovany znak

# konec cykly
# je cas vypsat heslo
print("Vase heslo je:", heslo)
