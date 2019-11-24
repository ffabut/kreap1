# Lekce 7

## Moduly

Moduly (knihovny, package) jsou hotové celky kódu, které můžeme vložit do našeho kódu, začít používat jejich funkce a tím si ušetřit mnoho práce.
Python v základu nabízí velké množství modulů, které můžeme použít - stačí je pouze naimportovat a to je vše.
Současně s tím, ale můžeme používat i neoficiální moduly cizích programátorek a programátorů, nebo vytvářet a znovu-používat moduly naše vlastní.
Tak jako funkce zaobaluje určitou část kódu do kompaktního celku, tak i moduly zaobalují celé funkce a velké kusy kódu do jednoho velkého celku - modulu.

## Importování modulů

Chceme-li používat modul, musíme jej prvně naimportovat - tím Pythonu řekneme, že máme o tento modul zájem a budeme jej využívat.
Python poté vloží kód tohoto modulu do našeho souboru a my jej můžeme používat.
K importování modulů používáme klíčové slovo `import`:

```python
import random # importujeme vestavěný modul random
# modul se chova podobne jako promenna, po importovani se vyskytuje pod svym jmenem
# k funkcim a objektum v modulu pristupujeme pomoci tecky - napriklad: random.randint(), random.random(), random.choice()

# kdyz je modul naimportovany, muzeme zacit pouzivat funkce, ktere obsahuje
i = random.randint(0,1000) # modul random obsahuje funkci randint(), ktera generuje nahodna cisla
print(i) # vypiseme nahodne cislo

f = random.random() # funkce random z modulu random vypisuje nahodne desetinne cislo float mezi 0 a 1
print(f)

seznam = [0, 2, 4, 6, 8, 10, 9999]
nahodnyPrvek = random.choice(seznam) # funkce choice() z modulu random vybira nahodne prvek ze seznamu/tuple/libovolne kolekce, ktery predavame jako argument funkci
print(nahodnyPrvek) # vypise nahodne vybrany prvek ze seznamu
```
