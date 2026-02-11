# Lece 4

## Funkce

Funkce umožňují zabalit určitou část kódu a pak ji moct volat/spouštět z různých míst v programu.

Také nám umožňují tento kód parametrizovat - spouštět s různými počátečními hodnotami a tak mírně měnit jeho průběh, to co dělá.
Funkce jsme již několikrát použili (print, input atd.), podíváme se proto prvně podrobněji na to, jak funkce používat - volat je, a poté se budeme věnovat tomu, jak vytvářet vlastní funkce.

Každá funkce:
- má své jméno,
- může definovat parametry a být volána s žádným, jedním či více argumenty - oddělujeme je čárkou,
- může mít návratovou hodnotu - výsledek,
- pokud funkce nevrací hodnotu, pak python i tak vrátí hodnotu `None`.

Pozn.: Termín "argument" se používá pro hodnotu, kterou posíláme do funkce, termín "parametr" se používá pro název, který funkce používá pro tuto hodnotu.
V praxi se ale tyto termíny často zaměňují, a není to velký problém, pokud je z kontextu jasné, co je myšleno.

### Volání funkce

Nejjednodušší je volání funkce bez argumentu a bez uložení návratové hodnoty, vypadá to takto:

```python
# voláme funkci, která se jmenuje print()
print() # prázdné závorky jsou nutnost
```

Předešlá funkce, jak již víme, vypíše prázdný řádek.
Zkusíme tedy přidat argument, toto jsme již také dělali:

```python
# voláme funkci print s jedním argumentem
print("Hello World!") # argument je textový řetězec "Hello World!"

# jako argument ale můžeme použít také proměnou
pozdrav = "Čau světe!"
# voláme funkci print s jedním argumentem
print(pozdrav) # argumentem je proměnná pozdrav, která odkazuje k hodnotě "Čau světe!"
```

### Návratová hodnota funkce

Funkce `print()` má za úkol tisknout do příkazové řádky, má něco vykonávat, nikoli počítat.
Funkce `print()` tak nemá návratovou hodnotu, nebo přesněji: její návratovou hodnotou je `None`, kterou Python automaticky vrací, když funkce nedefinuje jinou hodnotu.

```python
navratovaHodnota = print("Hello world")
print(navratovaHodnota)
```

Existují ale i funkce, které se zaměřují spíše na výpočet, než na vykonávání nějaké akce, a jejich hlavním smyslem je vracet nějakou hodnotu.
Příkladem funkce, která spíš nic nedělá a místo toho jde o její výsledek, tedy o její návratovou hodnotu, je například built-in funkce `pow()`:

```python
# funkce pow() mocni cislo na x-tou, prvním parametrem je mocněnec, druhým parametrem je mocnitel:
# pow(mocnenec, mocnitel)

# volame funkci pow() se dvema argumenty - 2 a 4
navratovaHodnota = pow(2, 4) # pow(2,4) má význam stejný jako 2**4, tedy dva na čtvrtou = 16

# muzeme si predstavit, ze vysledkem, navratovou hodnotou, python za behu programu nahradi volani funkce
# vlastne se tedy stane:
# navratovaHodnota = pow(2, 4)
# navratovaHodnota = 16

# navratova hodnota neni None, ale je to integer - výsledek po mocnění
print(navratovaHodnota)
```

### Parametry funkce
Parametry, které funkce definuje, a tím říká, jaké hodnoty neboli argumenty, musí být při volání funkce poskytnuty, jsou rozdílné funkci od funkce.
Pokud si nejsme jistyi, anebo používáme funkci poprvé, je ideální se podívat do dokumentace k dané funkci, kde se dozvíme, jaké parametry funkce definuje a k čemu jsou použity, a jaké argumenty tedy musíme poskytnout, aby funkce fungovala, jak chceme.
Případně se také můžeme podívat přímo do kódu funkce, což někdy může být rychlejší, než hledat v dokumentaci.
U složitějších funkcí ale dokumentace bývá přehlednější, než kód, který může být komplikovaný a těžko pochopitelný.

---

Některé funkce definují své parametry tak, že po nás vyžadují přesný počet argumentů a dokonce přesný datový typ, jinak dojde k chybě.

Příkladem takové funkce může být `hex()`, která převádí integer a pouze integer na [hexadecimální](https://cs.wikipedia.org/wiki/%C5%A0estn%C3%A1ctkov%C3%A1_soustava) string:
```python
result = hex(2026)
print(result) # '0x7ea'
```

Pokud `hex()` nedostane žádný argument, nebo dostane více než jeden argument, nahlásí chybu:
```python
result = hex() # TypeError: hex() takes exactly one argument (0 given)
result = hex(2026, 5) # TypeError: hex() takes exactly one argument (2 given)
```

Pokud `hex()` dostane argument, který není integer, nahlásí také chybu:
```python
result = hex(3.14) # TypeError: 'float' object cannot be interpreted as an integer
result = hex("2026") # TypeError: 'str' object cannot be interpreted as an integer
```
---

Jiné funkce zvládnout určitý rozsah počtu parametrů. (Realizováno skrze defaultní hodnotu parametru, default arguments - viz níže.)
Například `pow()` zvládne od dvou do tří argumentů:

```python
pow(5, 3)    # == 125, ekvivalent 5**3
pow(5, 3, 2) # == 1, ekvivalent 5**3 % 2, ale rychlější, je trochu divné/nečekané, že toto funkce pow() umí, ale umí to
```

---

Některé funkce zvládnout téměř neomezené počty argumentů. (Realizováno skrze *args a **kwargs - viz níže.)
Příkladem budiž nám dobře známý `print()`:

```python
print(None, True, "dva", 3, 4.0)
```

Funkce `print()` je také dobrým příkladem funkce, která zvládne různé datové typy argumentů, a to i v rámci jednoho volání funkce, jak vidíme výše.
Pro některé funkce dává smysl očekávat pouze určitý datový typ argumentu, jiné mohou akceptovat několik různých datových typů pro argument, pro jiné funkce je to jedno, a fungují s různými datovými typy.
To hodně záleží na konkrétní funkci, a je to opět něco, co se dozvíme z dokumentace, nebo zkoumáním kódu funkce.

---
Až doposud jsme argumenty funkce určovali pouze jejich pořadím, ale některé funkce nám umožňují určit argumenty i jejich jménem.

To si můžeme ukázat na funkci `print()` a jejích extra argumentech `end` a `flush`.
Argument `end` nám umožňuje určit, jaký text se má vytisknout na konci výstupu, pokud tento argument nezadáme, pak je defaultně použit nový řádek (`"\n"`).
Argument `flush` nám umožňuje určit, zda se má výstup okamžitě zobrazit, nebo ne - defaultně je nastaveno na `False`, což znamená, že se výstup nemusí zobrazit okamžitě, ale až později, například až když se naplní buffer.

```python
import time

print(f"TRI", end="\r", flush=True)
time.sleep(1)
print(f"DVA", end="\r", flush=True) # \r nám umožňuje přepsat předchozí výstup, takže se predchozi text "TRI" prepise textem "DVA"
time.sleep(1)
print(f"JEDNA", end="\r", flush=True)
time.sleep(1)
print(f"START!", end="\r", flush=True) 
```

Poznamka: "\r" nebo carriage return nefunguje v IDLE, je potřeba náš program spustit v terminálu, PowerShellu, nebo v jiném prostředí příkazové řádky, které tento znak podporuje. 
Pro víceřádkové výstupy je namísto "\r" vhodnější použít několikrát za sebou posun kurzoru na začátek předchozího řádku - `"\033[F"` (https://en.wikipedia.org/wiki/ANSI_escape_code#Control_Sequence_Introducer_commands).
Pro podrobnější vysvětlení se podívejte na příklady [examples/premazavani_textu](../examples/premazavani_textu).

### Built-in funkce

Python obsahuje předdefinované, built-in funkce, které můžeme rovnou použít.
Některé z nich již známe:
- print() - tiskne do příkazové řádky
- input() - čeká na vstup uživatele z příkazové řádky, může mít parametr, který uvede vstup: `input("zadejte jméno:")`

- int() - převede float, případně string obsahující pouze číslo, na integer
- float() - převede integer, případně string obsahující pouze číslo, na float
- str() - převede integer nebo float na string
- bool() - převede integer, float, string na bool(), False = 0, 0.0, "", všechno ostatní je True

- abs() - absolutní hodnota
- sum() - součet z kolekce čísel - například sum([1, 2, 3]) vrátí 6, kolekce však vysvětlíme v pozdějších lekcích
- pow() - mocnina
- round() - zaokrouhlení
- min() - minimum z několika hodnot
- max() - maximum z několika hodnot

- type() - výpis datového typu proměnné/hodnoty
- reversed() - otočení kolekce/iterátoru

- ord() - převod znaku na integer (unicode code point) - opak funkce chr()
- chr() - převod integeru (unicode code point) na znak - opak funkce ord()
- hex() - převod integeru na hexadecimální string
- oct() - převod integeru na oktalový string
- bin() - převod integeru na binární string

Python obsahuje i velké množství dalších užitečných built-in funkcí, ke kterým se dostaneme později - souvisejí s pozdějšími tématy.
Můžete se na ně podívat však i nyní v dokumentaci Pythonu: https://docs.python.org/3/library/functions.html


### Vlastní funkce - definice funkce
Kromě built-in funkcí můžeme vytvářet - definovat naše vlastní funkce.
To se hodí, pokud určitou část kódu, určitý úkon nebo funkcionalitu, chceme v programu používat víckrát na různých místech. 

Vlastní funkce vytváříme jejich definováním pomocí klíčového slova `def`, za nímž následuje název funkce s kulatými závorkami obsahující čárkami oddělené parametry (pokud nějaké jsou).
V nejjednodušší podobě můžeme definovat funkci bez parametrů takto:

```python
# definujeme vlastni funkci s nazvem mojeFunkce
def helloFunkce():
    print("Hello! a to je vse, co tato funkce umi")

# po definovani muzeme funkci pouzivat (stejne jakoby byla build-in, jiz v tom neni rozdil)
helloFunkce() # v tuto chvili program jakoby skoci do bloku helloFunkce, provede jej
# a pote bude ZDE pokracovat na dalsim radku
```

Tato funkce nemá žádné parametry a nevrací žádnou hodnotu.
Její poslání je pouze tisknout předem připravený text.
Jak bychom ji mohli rozšířit, aby tiskla námi zadaný text?

#### Definování parametrů funkce

Chceme-li, aby funkce přijímala nějaký argument, stačí jeho jméno uvést v závorkách při definici funkce:

```python
# definujeme funkci helloFunkce a v zavorce uvadime, ze bude prijimat jeden argument, kteremu jsme dali nazev jmeno
def helloFunkce(jmeno):
    pozdrav = "Hello " + jmeno + "!" # k argumentu pristupujeme jako k normalni promenne, ktera ale existuje pouze v tele funkce
    print(pozdrav)

helloFunkce("Beth")
helloFunkce("John")
```

Funkce může mít nula, jeden, ale i více argumentů, v takovém případě jednotlivé názvy argumentů oddělujeme čárkami:

```python
def collectiveHello(name1, name2, name3):
    pozdrav = "Hello " + name1 + " " + name2 + " and " + name3 + "!"
    print(pozdrav)
```

Datový typ argumentu není v základě nijak omezen.
Pokud budeme používat naše nebo cizí funkce, je to na nás, abychom si zjistili, jaký typ pro daný argument můžeme použít.
Poznámka: V Pythonu 3.5 byla přidána možnost určit, jaký typ daný argument vyžaduje - budeme se tomu věnovat později.


##### Defaultní hodnota argumentu

Občas se může hodit definovat základní hodnotu argumentu nebo argumentů.
Výhodou je, že v takové případě funkce nevyžaduje s těmito argumenty - obejde se bez nich.
Chceme-li argumentu přiřadit výchozí hodnotu, pak napíšeme za název argumentu rovná se a uvedeme hodnotu, podobně jako bychom definovali proměnnou:

```python
def helloFunkce(name="user"):
    pozdrav = "Hello " + name + "!"
    print(pozdrav) 

helloFunkce() # vytiskne "Hello user!"
helloFunkce("Jane") # vytiskne "Hello Jane!"
```

Pozor: všechny argumenty s defaultními hodnotami musí být uvedeny až po všech argumentech, která defaultní hodnoty nemají:

```python
# vsechny argumenty bez defaultni hodnoty jsou uvedeny jako prvni a potom az ty s defaultni hodnotou
# vse je tedy ok
def collectiveHello(name1, name2="user", name3="user"):
    pozdrav = "Hello " + name1 + " " + name2 + " and " + name3 + "!"
    print(pozdrav)

collectiveHello("Jane")
collectiveHello("Mustafa", "Jane")
collectiveHello("John", "Jane", "Ian")
```

Tato definice by ale neprošla, argumenty s defaultní hodnotou předchází argumentu bez defaultní hodnoty:

```python
def collectiveHello(name1="user", name2="user", name3): #name3 nema defaultni hodnoty a pritom je po argumentech, ktere ji maji, zde python nahlasi chybu
    pozdrav = "Hello " + name1 + " " + name2 + " and " + name3 + "!"
    print(pozdrav)

collectiveHello("Jane")
collectiveHello("Mustafa", "Jane")
collectiveHello("John", "Jane", "Ian")
```

##### Nekonečné množství argumentů
Pokročilé: Občas se nám může hodit funkce, která umí přijímat neomezené množství argumentů.
Jednu takovou funkci již známe - ano, je to print().
Jak podobné chování můžeme realizovat?

```python
def greet(*names):
    for name in names:
        print("Hello", name)

greet("Jane", "Patrick", "Olia", "Michael")
```

##### Nekonečné množství pojmenovaných argumentů
Pokročilé: Může se nám také hodit mít funkci, do které můžeme poslat větší množství pojmenovaných parametrů.
Například pro detailní konfiguraci funkce, nebo argumenty potřebují jak hodnotu, tak i klíč/key neboli jméno argumentu.
Jde vlastně o neomezené množství pojmenovaných argumentů.

To můžeme realizovat pomocí **kwargs:

```python
def myfunc(**kwargs):
    # kwargs is a dictionary.
    for k,v in kwargs.items():
         print(f"jmeno argumentu={k}: hodnota={v}")

myfunc(abc=123, efh=456)
# jmeno argumentu=abc: hodnota=123"
# jmeno argumentu=efh: hodnota=456"
```

#### Návratová hodnota funkce

Zatím jsme definovali funkce, které něco dělají, ale nevrací žádné výsledky.
Co kdybychom ale potřebovali funkci, která má něco spočítat, jak získat její výsledek?

K tomu, aby funkce vracela nějaký výsledek - měla návratovou hodnotu užíváme klíčové slovo `return`, po kterém následuje hodnota, která se má vrátit:

```python
def naDruhou(x): # funkce ma jeden argument x
    vysledek = x ** 2 # zde vypocitame druhou mocninu argmumentu x a ulozime do promenne vysledek
    return vysledek # zde funkce vraci hodnotu, ktera je v promenne vysledek

a = naDruhou(5) # vysledek 
print(a) # vytiskne 25
```

##### Více návratových hodnot

V Pythonu existuje více možností jak funkcí vracet více než jednu hodnotu.
Jednou ze základních možností je nechat funkci vracet typ sekvence `tuple`, tj. seřazený neměnný seznam.
V takovém případě můžeme jednotlivé návratové hodnoty po `return` oddělit čárkou:

```python
def ctyriOperace(a, b):
    soucet = a + b
    soucin = a * b
    rozdil = a - b
    podil  = a / b

    return soucet, soucin, rozdil, podil

vysledek = ctyriOperace(2, 5)
print(vysledek) # vytiskne: (7, 10, -3, 0.4), tj. vytiskne tuple obsahujici 4 hodnoty

# alternativne muzeme hodnoty rovnou priradit do 4 promennych:
a, b, c, d = ctyriOperace(2, 5)
print(b) # vystikne soucin, tj. 10

# muzeme klidne nekterou hodnotu vynechat a to pomoci podtrzitka:
_, _, c, _ = ctyriOperace(2, 5)
print(c) # vytiskne -3
```

## Metody

Metody jsou funkce, které jsou dostupné v objektech (podrobně probereme později).
Prozatím se zaměříme na to, že datové typy v pythonu jsou objekty - a tedy datové typy mají své specifické metody - funkce.

Zkusíme například využít metody upper() dostupnout v strings:

```python
pozdrav = "Hello world!" # je to málo nahlas, chceme capslock
pozdrav = pozdrav.upper() #pozdrav je typu string, typ string obsahuje metodu upper(), kterou nyní voláme
print(pozdrav) #vytiskneme

# můžeme ale volat i přímo na string hodnotě, nikoli proměnné, například:
print("A taky česky: Zdar světe!".upper())
```

---

Podrobněji se built-in metodám jednotlivých datových typů budeme věnovat později.
Prozatím nám stačí vědět, že se metody chovají téměř stejně jako funkce, avšak jsou dostupné pouze na jednotlivých specifických objektech, tj. string obsahuje metody upper(), avšak integer žádnou takovou metody nemá (ani by nedávala pro integer smysl).

## Procvičování

Úkol1: Napište funkci, která sčítá dvě čísla.
Řešení [zde](ukol1.py).

---

Úkol 2: Napiště funkci, která pozdraví uživatelku jejím jménem, je možné nastavit počet pozdravů, v základě je to ale jeden pozdrav.
Budete nejspíše potřebovat dva parametry: jméno a počet opakování pozdravu.
Ve funkci poté asi použijete některý z cyklů.
Řešení [zde](ukol2.py).

---

Úkol 3: Napište funkci, která umí pozdravit dva uživatele.
Umožňuje nezadat jméno druheho uživatele, pak pozdravi jen jednoho.
Řešení [zde](ukol3.py).

---

Úkol 4: Napiště dvě funkce, které volají jedna druhou a sledujte chaos při jejich zavolání.
Tj. funkce1 dělá cokoliv, například vypisuje něco do příkazové řádky, na svém konci v ní voláme funkci2().
Funkce2 dělá cokoliv, ale na svém konci volá zpět funkci1().
Při zavolání funce1 nebo funkce2 se proces zacyklí - funkce se budou navzájem neustále volat a nikdy neskončí.
Řešení [zde](ukol4.py).
