# Lekce 7

## Moduly

Moduly (knihovny, package) jsou hotové celky kódu, které můžeme vložit do našeho kódu, začít používat jejich funkce a tím si ušetřit mnoho práce.
Moduly můžeme rozdělit do 3 kategorií:
- lokální
- standardní/built-in
- externí

Python v základu nabízí velké množství standardních modulů, které můžeme rovnou použít - stačí je pouze naimportovat a to je vše.
Současně s tím, ale můžeme používat i neoficiální moduly cizích programátorek a programátorů, nebo vytvářet a znovu-používat moduly naše vlastní.
Tak jako funkce zaobaluje určitou část kódu do kompaktního celku, tak i moduly zaobalují celé funkce a velké kusy kódu do jednoho velkého celku - modulu.

### Lokální moduly
Pokud se náš kód rozroste, může se nám hodit jej rozdělit do více souborů.
Jak ale poté přistupovat ke kódu, který je v odděleném souboru?
Stačí jej naimportovat.

Mějme hlavní soubor `main.py` (tento soubor je vstupní, právě jej voláme např. skrz `python main.py`) a vedlejší soubor `printing.py`, ve kterém udržujeme dodatečný kód.

```python
#printing.py

def hello_world():
    print("Ahoj světě!")
```

```python
#main.py

import printing

printing.hello_world() # voláme funkci hello_world() umístěnou v souboru printing.py
```

Tímto způsobem si můžeme rozčlenit náš program do několika menších souborů.
Ideální je soubory smysluplně pojmenovat a udržovat v nich kód relevantní k jejich názvu, tématicky podobný, s podobnou fukcionalitou apod.
Ale tato volba je pouze na nás.

Ideální také je nevolit názvy, které kolidují s názvy built-in funkcí a jiných modulů, volit něco unikátního, abychom si nepřepsali například modulem `print.py` jméno funkce print() a tím se zbavili možnost volat funkci print().
Např.:

```python
#main.py

import print # import modulu print.py

print.hello_world() # tohle projde, pokud v print.py máme definovanou funkci hello_world()

print("Uspesne naimportovano a pouzito!") #ale tohle selze, protoze pod jmenem print uz neni dobre znama funkce print()
#ale je tam modul print.py a ten nemuzeme primo volat jako funkci - reseni je modul pojmenovat jinak
```

Alternativně můžeme také použít konstrukt `import x as y` a importovat tak pod jiným jménem než se jmenuje samotný modul/soubor:

```python
import print as my_print #import modulu print.py, ale pod jmenem my_print

my_print.hello_world() #k modulu ted pristupujeme pod jmenem my_print

print("Uspesne naimportovano a pouzito!") #tohle projde, protoze pod jmenem print() je porad dobre znama built-in funkce
```



### Standardní / Built-in moduly

Standardní funkce v Pythonu jako print(), input() a reverse() jsou absolutním minimem, které ale nepokrývá všechny potřeby - například dělání HTTP requestů, stahování atd.
Tato obecná, ale přeci jen specializovaná funkcionalita je schována do standardních modulů, které jsou součástí Pythonu, ale je potřeba je explicitně naimportovat.

Python obsahuje velké množství standardních built-in modulů, jejich kompletní seznam je k nahlédnutí na [Python Module Index](https://docs.python.org/3/py-modindex.html).
Nyní se pokusíme stručně podívat alespoň na některé z nich.
Nejde o pořádné ponoření se do těchto modulů, ale spíše takový inspirativní náhled na to, co Python skrze built-in moduly umožňuje.

#### Importování modulů

Chceme-li používat standardní modul, musíme jej prvně naimportovat - tím Pythonu řekneme, že máme o tento modul zájem a budeme jej využívat.
Python poté vloží kód tohoto modulu do našeho souboru a my jej můžeme používat.
K importování modulů používáme opět klíčové slovo `import`:

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

#### random

Modul random umožňuje pracovat s náhodou a náhodnými čisly.

##### Nahodne float cislo 0-1
```python
import random

random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")
```

##### Nahodne cele cislo
```python
import random

random_int = random.randint(1, 10)  # Random integer between 1 and 10 (inclusive)
print(f"Random integer between 1 and 10: {random_int}")
```

##### Nahodny prvek z kolekce
```python
import random

colors = ['red', 'blue', 'green', 'yellow']
random_color = random.choice(colors)
print(f"Randomly chosen color: {random_color}")
```

##### Nohodne promichani kolekce
```python
import random

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")
```

##### Nahodne float cislo v danem rozsahu
```python
import random

random_float_in_range = random.uniform(1.5, 5.5)
print(f"Random float between 1.5 and 5.5: {random_float_in_range}")
```

##### Nahodna pod-cast z kolekce
```python
import random

fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
random_sample = random.sample(fruits, 3)  # Choose 3 unique elements
print(f"Random sample of 3 fruits: {random_sample}")
```

#### URLIB

Slouží pro dělání HTTP requestů na internetové servery a stahování souborů.
Obecně je ale praktičtější použít externí modul Requests.

```python
from urllib.request import urlopen

with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline
```

#### 


### Externí moduly

Externí moduly jsou moduly dostupné z balíčkovacího systému pip.
Tyto moduly je prvně potřeba nainstalovat pomocí pip a poté je naimportovat.
