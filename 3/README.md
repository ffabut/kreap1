# Lekce 3

Tato lekce se zaměří na téma větvení programu - řízení toku programu, tedy schopnost programu reagovat na různé situace různými způsoby.
Základními nástroji pro řízení toku programu jsou:
- podmínky (IF)
- cykly (WHILE, FOR).

## Podmínky

Podmínky umožňují vykonat určité části kódů (blok kódu) pouze v případě, když platí určitá logická podmínka - například větší než, nebo rovno, případně pokud použitá proměnná má hodnotu True.

### Jednoduchá podmínka IF
Nejjednodušeji podoba podmínky užívá jedno klíčové slovo `if`.


```python
cislo = 120

if cislo > 10: # vyraz cislo>10 vraci hodnoty True nebo False, pokud vrati True, vykona se odsazena cast kodu
    print("cislo je vetsi nez 10!") # tyto odsazene radky se vykonaji pouze pokud platila podminka 
    print("a to je dobre") # tyto odsazene radky se vykonaji pouze pokud platila podminka
    # zde může pokračovat libovolný počet příkazů podmínky

# zde jiz pokracuje program za vsech okolnosti
print("jedem dál...")
```

případně můžeme též použít například:

```python
cislo = 120
vetsi_nez = cislo > 10 # vyraz vrati True
if vetsi_nez: # pokud vetsi_nez je True (v tomto pripade ano), vykona se odsazena cast kodu
    print("cislo je vetsi nez 10!")
    print("a to je dobre")

# zde jiz pokracuje program za vsech okolnosti
print("jedem dál...")
```

Všimněme si odsazení bloku následujícího po dvojtečce.

Syntax `if` vypadá takto:
- začneme klíčovým slovem if
- za něj umístíme libovolný logický výraz
- ukončíme dvojtečkou - tím určíme, že chceme pokračovat sadou/blokem příkazů na dalším řádku
- na dalším řádku odsadíme kód o 4 mezery (případně jiný počet, ale vždy stejný)
  - napíšeme příkaz
  - pokud chceme více příkazů, odsadíme na dalším řádku stejný počet mezer a napíše další příkaz
  - dokud jsme odsazení, do té doby jsme v bloku, který se vykoná pouze v případě, že platí podmínka
- chceme-li podmínku ukončit, pak na novém řádku přestaneme odsazovat, tato část se již vykoná v každém případě

---
Úkol 1: napište program, který vypíše zda je proměnná `x` větší nebo menší než 100.
Budete nejspíše potřebovat 2 podmínky IF. (Řešení pro kontrolu [zde](ukol1.py).)

### Podmínka IF-ELSE
Podmínku `IF` je možné rozšířit klíčovým slovem `ELSE`, abychom mohli zachytit a reagovat na situaci, kdy podmínka neplatí.
Můžeme tak jednou konstrukcí reagovat na oba výsledky podmínky - na True i na False a nemusíme používat 2x IF:

```python
cislo = 2

# vykona se bud kod v IF nebo kod v ELSE
if cislo > 10:
    print("Cislo je vetsi nez deset!") # vykona se, pokud podminka cislo>10 je True
else:
    print("Cislo neni vetsi nez deset!") # vykona se, pokud se nevykonala predchozi podminka, tedy v situaci False

print("pokracujem...")
```

Všimněme si, že za else je dvojtečka a blok příkazů za else je odsazen.

### Podmínka IF-ELIF-ELSE
Podmínku můžeme ještě rozšířit libovolným počtem konstruktů `ELIF`.
Jde o dodatečné podmínky IF, které se vykonají pouze v případě, že se předchozí podmínky nevykonaly a zároveň pokud podmínka v `ELIF` je pravdivá.
Můžeme tak v jednom konstruktu IF-ELIF-ELSE reagovat na velké množství situací:

```python
cislo = -10

if cislo > 10:
    print("cislo je vetsi nez 10")
elif cislo < 0:
    print("cislo je mensi nez 10 a je zaporne")
elif cislo < 10:
    print("cislo je mensi nez 10")
elif cislo == 10:
    print("cislo je rovno 10")
else:
    print("tato situace by za vyse zadanych podminek nemela nastat")

print("pokracujem...")
```

Vsimneme si, ze za klicovym slovem `elif` nasleduje podminka / logicky vyraz, pote dvojtecka a nasledujici blok prikazu je odsazen.

Ve vyse uvedenem priklade by cast kodu `else` nemela nikdy nastat - pro kazde cislo bude platit vzdy jedna z podminek a else tak nenastane.
Pro tyto případy můžeme `else` vynechat:

```python
cislo = -10

if cislo > 10:
    print("cislo je vetsi nez 10")
elif cislo < 0:
    print("cislo je mensi nez 10 a je zaporne")
elif cislo < 10:
    print("cislo je mensi nez 10")
elif cislo == 10:
    print("cislo je rovno 10")

print("pokracujem...")
```

## Klíčové slovo pass

Občas se nám může stát, že některém bloku nechceme nic provést.
Nemůžeme ale do bloku nic nenapsat, s tím by měl python problém, tento kód nebude fungovat:

```python
heslo = 12345 # slabe heslo...

if heslo == 12345:
else:
    exit() # funkce exit slouzi k okamzitemu ukonceni programu

print("část programu pro zasvěcené...")
```

Python nám vyhodí chybu: `IndentationError: expected an indented block`, jelikož po dvojtečce na řádky IF očekává odsazení a blok kódu.

Abychom vytvořili blok, ale zároveň nemuseli zadávat žádný příkaz, je v Pythonu přítomný příkaz `pass`.
Ten je jednoduše příkazem, který říká, že se nic nemusí dělat.
Blok tak existuje, ale zároveň se v něm nic neděje:

```python
heslo = 12345

if heslo == 12345:
    pass
else:
    exit()

print("část programu pro zasvěcené...")
```

Poznámka: problém jsme mohli také řešit otočením logické podmínky, což by bylo asi elegantnější a zároveň by to nevyžadovalo `pass`.

```python
heslo = 12345

if heslo != 12345: # pokud se heslo nerovná 12345
    exit()

print("část programu pro zasvěcené...")
```

---

Úkol 2: napiště program, který otestuje, zda je uživatel člověk.
Nejspíše použijete funkci `input()`, podmínku IF-ELIF-ELSE a funkci exit().
(Řešení pro kontrolu [zde](ukol2.py).)


## Cykly

Cykly nám umožňují několikrát opakovat určitou stejnou část kódu.

### Cyklus While

Cyklus `while` opakuje kód, dokud je podmínka cyklu pravdivá:

```python
i = 0

while i < 100: # pokud je podmínka pravdivá, cyklys while vykoná všechny příkazy v dalším bloku a poté se vše zopakuje - opět se otestuje podmínka atd...
    print(i) # vypiseme promennou i 
    i = i + 1 # zvetsime promennou i o 1, cyklus se zopakuje

print("a to je vse...") # kdyz podminka neni pravdiva, cyklus se ukonci a program pokracuje dal v kodu
```

Mohli bychom říct, že cyklus `while` je tak trochu podmínka, která se opakuje dokud nepřestane platit.
To je také drobný zádrhel při použití cyklu `while` - musíme si dát pozor, aby podmínka někdy přestala platit - často v rámci cyklu upravujeme nějakou proměnnou, která je součástí podmínky.
Pokud si nadáme pozor, může cyklus běžet donekonečna, což tedy někdy může být také záměr - zkuste to v příkladu č. 3 níže.


---
Úkol 3: Napiště program, který bude postupně počítat do nekonečna.
Poznámka: možná budete potřebovat program "násilně" ukončit, k tomu jde v příkazové řádce použít příkaz ctrl-c, případně command-c.
(Řešení pro kontrolu [zde](ukol3.py).)

### Cyklus for

Cyklus `for` slouží k procházení skrz kolekce objektů (seznamy, slovníky a podobně - budeme se ji věnovat později) - ve zkratce ale jde o proměnné, které obsahují více seřazených či neseřazených hodnot - například seznam studentek a studentů a podobně.
Prozatím ale využijeme toho, že datový typ `string` je v podstatě seznamem znaků/písmen a budeme tak procházet skrze řetězce string.

Jednoduchý cyklus for vypadá například takto:

```python
jméno = "Ladislava Pěchoučková"

for znak in jméno: # postupně vezme každý znak v řetězci jméno, uloží jej do proměnné znak a pak vykoná blok příkazů
    print(10*znak) # v prvním běhu je znak=="L", poté znak=="a", pak znak=="d" atd....

print("KONEC")
```

Cyklus začíná klíčovým slovem `for`, po něm následuje jméno proměnné, do které se postupně bude ukládat každý prvek obsažený v kolekci uvedené po klíčovém slovu `in`, vše ukončeno dvojtečkou a odsazeným blokem příkazů.

## Zanořování kódu - podmínek do cyklů a naopak

Občas se dostaneme do situace, že potřebujeme v cyklu podmínku či naopak, potřebujeme bloky kódu zanořit do sebe.
V základě se nic nemění, pouze zanořený blok odsadíme o další 4 mezery, například takto:

```python
for znak in "Ladislava Pěchoučková":
    # blok - tělo cyklu je odsazeno 4 mezerami
    # vytvoříme podmínku
    if znak == "a":
        print(10*znak) # blok - tělo podmínky je odsazeno o další 4 mezery navíc než blok, v kterém se nachází
    else:
        print(znak) # stejně tak je navíc odsazeno else

    print("zbytek příkazů, které mají být v těle cyklu, je odsazen 4 mezerami")

print("a zde jsme již zpátky v normálním běhu programu")
```

Zanořit můžeme i dva cykly do sebe:

```python
for znak in "Zikmund Pechánek":
    x = 1
    while x < 10:
        print(x*znak)
        x = x + 1
```

A samozřejmě i dvě podmínky:

```python
x = 132

if x % 2 == 0:
    print("číslo je dělitelné 2")
    if x % 3 == 0:
        print("a navíc je i dělitelné 3!")

print("konec")
```

---

Zanořovat samozřejmě můžeme i více než 2 úrovně cyklů a podmínek.
Výraznějšímu zanoření je ale lepší se vyhýbat, kód pak začíná být těžce srozumitelný a můžeme začít dělat chyby, které nebudou na první pohled dobře patrné.

### Break - Předčasné ukončení cyklu

Cyklus můžeme předčasně ukončit pokud zavoláme příkaz `break`.

```python
x = 1000

while True: #místo logického výrazu / podmínky můžeme zapsat i True - pak vytvoříme nekonečný cyklus While
    x = x + 1
    if x / 13 = 1234: # pokud je výsledek 1234
        break # tak se cyklus ukončí

print(x, "po dělení 13 je 1234")
```

#### Cykly for a while rozšířené o else

Cykly for a while je možné rozšířit o tvrzení `else`.
To se v tomto případě ale chová lehce neintuitivně - kód v bloku else je spuštěn pokaždé, když cyklus neskončí neočekávaně příkazem break.
Dalo by se říct, že by se `else` v tomto případě mělo jmenovat spíše `no-break`.

Else statement v cyklech není příliš intuitivní a vyloženě praktický a tak není potřeba si jej vyloženě pamatovat...

##### For-else

Ukázka užití else v cyklu for, zkuste si jej spustit postupně se všemi třemi textovými řetězci (ostatní za/odkomentujte #).
V prvním případě cyklus proběhne 4x a neskončí skrze `break`, tedy se vykoná i příkaz v else.
V druhém případě cyklus neproběhne ani 1x, ale přitom neskončí skrze `break`, a tedy se i zde vykoná příkaz v bloku else.
Ve třetím případě cyklus proběhne 3x, přičemž třetí průběh ukončí cyklus příkazem `break`, a tedy blok else se nevykoná:

```python
txt = "Ahoj"
#txt = ""
#txt = "BREAK"

for znak in txt:
    print(znak)
    if znak == "E":
        break
else:
    print("probehl else")
```

##### While-else

Else se u while chová stejně jako u for, v následujícím příkladu zkuste všechny 3 varianty proměnné i (zakomentujte nepotřebné hodnoty).

V prvním případě (i=1000) se běh zastaví na číslo 250, které se nedá dále dělit, zavolá se break a tedy se nevypíše výsledek, blok else se neprovede.
V druhém případě (i=0) cyklus neprovede ani 1x, a tedy neskončí skrze `break` a proto se blok `else` vykoná.
V třetím případě (i=8) se cyklus provede 2x (vypíše 4 a 2) a neskončí `break`, tedy se provede blok `else`, který vypíše, že výsledek je 2.

```python
i = 1000
#i = 0
#i = 8

# cyklus ma za ukol delit cisla, dokud jsou vetsi jak 2
while i > 2:
    i = i / 2
    print(i)
    if i % 2 != 0: #pokud číslo není dál dělitelné 2, cyklus se ukončí
        break
else:
    print("výsledek je:", i)
```

### Continue - předčasné ukončení jednoho opakování cyklu

Continue se používá v cyklech k předčasnému ukončení aktuálního průběhu cyklu - tedy neukončí celý cyklus, ale jen jeho právě probíhající iteraci.
Následující program vypisuje všechna čísla dělitelná 13 menší než 1000:

```python
i = 0
while i < 999:
    i = i + 1
    if i % 13 != 0: # pokud zbytek po deleni 13 neni 0, pak 
        continue # ukoncime tuto iteraci a jdeme na dalsi cislo

    print(i)
    # zde bychom mohli provadet slozitejsi vypocty a pak by uziti continue davalo vetsi smysl
```

Poznámka: v kódu nahoře by šlo použít i podmínku `if i % 13 == 0` a pak vypsat číslo.
Možná by to byla elegantnější varianta než použití `continue`, ale to je na našem vkuse a uvážení.

## Procvičování

Úkol 4: Udělejte lepší verzi programu, který ověřuje, zda je uživatel člověk nebo bot.
Nápověda: Může se vám hodit nekonečný cyklus while, podmínka a break. 
(Řešení pro kontrolu [zde](ukol4.py).)

Úkol 5: Napiště program, který z textového řetězce odstraní samohlásky a výsledek vytiskne.
Nemusíte řešit diakritiku a velká písmena.
Nápověda: Může se vám hodit for proměnná, loop a podmínka.
(Řešení pro kontrolu [zde](ukol5.py).)

## Další řízení

Zde již můžeme skončit, avšak pro úplnost Python obsahuje ještě pár další konstrukcí, jak řídit běh programu.

### Try-Except

Slouží pro spuštění kódu, který může dopadnout Exception (výjimkou, errorem).
V případě že v bloku try dojde k výjimce, kód přeskočí do části except.

```python

a = int(input("Zadejte cislo 0 az 10"))
try:
    vysledek = 100/a
    print(f"100/{a}={vysledek}")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")
```

### Match

Match je podobný statementu switch v jiných jazycích a v Pythonu je poměrně málo využívaný.
Ale pokud byste jej někdy někde viděli, jeho podoba je:

```python
status = 400
match status:
    case 200:
        print("OK!")
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")
```
