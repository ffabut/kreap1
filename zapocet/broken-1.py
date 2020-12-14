# Program: cvičení počítání
import random

def soucet(a,b):
    """
    Funkce přijímá dva argumenty a vrací jejich součet.
    """
    result = a + b
    return

levels = input("Kolik chcete hrát levelů?")
correct = 0

for x in range(levels): # kolik je levelů, tolikrát se zeptáme - range() generuje iterátor 0,1,2...
    a = random.randint(1,999)
    b = random.randint(1,999)

    otazka = "Kolik je " + a + "+" + b + " ?"
    result = int(input(otazka))

    if result == soucet(a, b): # pokud odpoved sedi s vysledkem, je vse dobre
        print("To sedí!")
        correct + 1 # zvysime pocet spravnych odpovedi o 1
    else: # jinak neni
        print("Nene...")

print("Z", levels, "jste měla/měl", correct, "správně.")
print("Úspěšnost =", str(levels/correct*100), "%")
