# Lekce 5

V této lekci se zaměříme na datové typy představující kolekce: Ntice, seznamy, množiny a slovníky.
Jde o datové typy vhodné v situacích, kdy pracujeme s více prvky - například seznamy lidí, překladové slovníky, množiny apod...

Kolekce - Ntice, seznamy, množiny a slovníky mohou jako své prvky obsahovat libovolný typ, různé kombinace různých typů.
A protože i kolekce jsou typem, tak mohou obsahovat kolekce obsahovat i jiné kolekce.
K tomu se dostaneme postupně...

## Kolekce představující posloupnosti

Jde o seřazené kolekce, každý jejich prvek má dané pořadí a na základě tohoto pořadí k němu můžeme přistupovat.
Kolekce představující posloupnosti jsou typy, které podporují operátor příslušnosti `in`, funkci pro zjištění velikosti `len()` a které jsou iterovatelné.
Při iteraci vracejí kolekce představující posloupnosti své prvky v určeném pořadí.

V základě se v Pythonu objevují dva typy představující posloupnosti: Ntice (Tuple) a Seznamy (List).
Chovají se téměř stejně s jednou výjimkou - Ntice (Tuple) jsou neupravitelné - nemůžeme měnit jejich obsah, u seznamu obsah měnit můžeme.

Jelikož jsou posloupnosti seřazené, můžeme Pythonu říct něco na způsob: z posloupnosti X chci 15. prvek, díky!

### N-tice / Tuple

Tuple je uspořádaná a neměnná kolekce 0 nebo více prvků.
Ntici definujeme jako normální proměnnou, avšak zadáme více hodnot a ty oddělíme čárkou:

```python
ntice = "nula", "jedna", 2, 3, "čtyři", 5.0
print(ntice) # vytiskne: ("nula", "jedna", 2, 3, "čtyři", 5.0)
```

Stejně tak je možné tyto hodnoty uzavřít do kulatých závorek:

```python
ntice = ("nula", "jedna", 2, 3, "čtyři", 5.0) # je víc jasné, že opravdu myslíme tuple, ale jinak se chová stejně jako bez závorek
print(ntice) # vytiskne: ("nula", "jedna", 2, 3, "čtyři", 5.0)
```

Varianta uzavřená do kulatých závorek je více jednoznačná a proto je asi lepší používat spíše ji.
Například při užívání tuple jako argumentu funkce by bez závorek mohla nastat chyba:

```python
def ocekavamTuple(ntice):
    print(ntice[0] # vypise prvni prvek Ntice

ocekavamTuple(1, 2, 3) # zde si python bude myslet, ze jde o tri argumenty a ve funkci pak nastane chyba
ocekavamTuple((1, 2, 3)) # zde je jasne, ze je argument jeden a je jim Tuple (1, 2, 3), vse bude OK
```

V případě delších Ntic, můžeme jednotlivé prvky ohraničené kulatými závorkami oddělovat novým řádkem, aby nebyly za sebou na příliš dlouhém jednom řádku, ale pod sebou ve sloupci:

```python
oblibeneUmelkyne = (
    "Christian Falsneas",
    "Markéta Wágnerová",
    "Jeremy Deller",
    "Hans Haacke"
) #je to stejne jako:

oblibeneUmelkyne = ("Christian Falsneas", "Markéta Wágnerová", "Jeremy Deller", "Hans Haacke")
```

#### Typy uložitelné do Ntice

Do Ntic a dalších kolekcí můžeme ukládat nejrůznější datové typy, jejich kombinace a dokonce i jiné Ntice, seznamy a další.

```python
ntice = (1, "dva", 3.0, True, None) # Ntice obsahujici nekolik ruznych typu

ntice = (2) # Ntice s jednim clenem, toto muzeme udelat i kdyz jsou Ntice nemenne
# duvodem je, ze neupravujeme predchozi Ntici, ale vytvarime novou a tu ukladame do promenne
# ntice[0] = 20 - toto by ale neslo: nemuzeme upravit prvni prvek Ntice, jelikoz Ntice je nemenna

a = 2
b = 3
tup = (a, b) # do ntice muzeme vlozit i cele promenne - ulozi se tam odkazy na konkretni hodnoty
print(tup) # vytiskne (2, 3)

b = 111 # pokud zmenime puvodni promennou, bude b odkazovat na 111
print(tup) # ale ntice stale odkazuje na puvodni hodnotu 3, takze opet vypise: (2, 3)
```

Jak již bylo řečeno, do Ntice můžeme uložit i jinou Ntici:

```python
skoly = (("FaVU", 3.6), ("AVU", 4.4), ("FU OSU", 5.0))
print(ntice[0]) # vypise prvni prvek Ntice skoly - jde o Ntici ("FaVU", 3.6)

print(ntice[0][1]) # vypise prvni prvek Ntice skoly a z nej druhy prvek, tedy vypise "3.6"
# alternativne muzeme klidne zapsat:

skola = skoly[0] # do promenne skola ulozi prvni prvek z ntice skoly - tuple ("FaVU", 3.6)
print(skola[1]) # z Ntice skola ("FaVU", 3.6) vypise druhy prvek - "3.6"
```

#### Přístup k prvkům v Ntici

Jelikož je Ntice uspořádaná, tak můžeme přistupovat k jejím jednotlivým členům pomocí indexu - jejich pořadí umístění v Ntici.
Index zadáváme do hranatých závorek za jménem Ntice:

```python
ntice = ("nula", "jedna", 2, 3, "čtyři", 5.0)
print(ntice[3])
print(ntice[0])
print(ntice[5])
```

---

Pozor: jak už je v programování zvykem, tak se začíná počítat od nuly.
První prvek má tedy index 0, pátý prvek má index 4 apod...  

#### Změna prvků v Ntici

Ntice jsou neměnné, což znamená, že nemůžeme měnit jejich obsah.
Pokud bychom chtěli změnit třetí prvek v Ntici, pak nastane chyba, toto nejde:

```python
ntice = ("nula", "jedna", 2, 3, "čtyři", 5.0)
ntice[2] = "dva" # zde nastane chyba!
```

#### Řezy

Občas nechceme přistupovat pomocí indexu pouze k jednomu prvku, ale k více prvkům.
V takové případě použijeme řezy - nebudeme specifikovat jednu hodnotu indexu, ale dvě hodnoty oddělené dvojtečkou - první hodnota označuje první prvek, od kterého začíná řez (včetně něho samého) a druhá hodnota označuje prvek po který řez trvá (bez tohoto prvku):

```python
ntice = ("nula", "jedna", 2, 3, "čtyři", 5.0)
print(ntice[1:4]) # vypise prvky s indexem 1, 2 a 3 (index 4 nikoliv)
```

Druhé číslo můžeme vynechat - v takovém případě bude řez obsahovat všechny prvky až do konce Ntice:

```python
ntice = ("nula", "jedna", 2, 3, "čtyři", 5.0)
print(ntice[1:]) # vypise prvky s indexem 2, 3, 4 a 5 - 5 je poslednim prvkem v Ntici, zde se skonci
```

Stejně tak můžeme vynechat i začáteční index, byť bychom mohli použít index 0:

```python
ntice = ("nula", "jedna", 2, 3, "čtyři", 5.0)
print(ntice[:2]) # vypise prvky s indexem 0, 1
print(ntice[0:2]) # vypise prvky s indexem 0, 1 - jde o totez jako ntice[:2]
```

##### Řezy a záporný index

Napiseme-li index s minusem, pak tim myslime poradi prvku od konce Ntice, napriklad:

```python
ntice = ("nula", "jedna", 2, 3, "čtyři", 5.0)
print(ntice[:-2]) # vypise prvky od prvniho a skonci pred druhym od konce: "nula", "jedna", 2, 3
print(ntice[-5:-1]) # vypise prvky od pateho od konce a skonci pred prvnim od konce: "jedna", 2, 3, "čtyři", 5.0
```

#### Operátor `in` pro zjištění příslušnosti prvku

Občas se hodí vědět, zda je prvek součástí množiny, k tomu slouží operátor `in`, jeho použití je následující:
`hodnota in Ntice`.
Pokud je hodnota stejna jako nektery z prvku Ntice (nebo seznamu, mnoziny ci slovniku), pak je vracena hodnota `True`, v opackem pripade `False`.

Ukázka použití:

```python
oblibenaCisla = (0, 13, 17, 9, 3, 7, -111)

if 18 in oblibenaCisla:
    print("Cislo je moje oblibene")
else:
    print("Cislo neni moje oblibene")
```

---
Úkol1: Napiště program, který zjistí, zda má uživatel stejného oblíbeného umělce jako vy.
Nejspíše použijete tuple, operátor in, funkci input().
Řešení [zde](ukol1.py).

#### Iterace přes prvky Ntice pomocí `for`

Častou operací s Nticemi (a seznamy, množinami a slovníky) je průchod přes jejich všechny prvky - iterace.
K tomu slouží cyklus `for`, užití je následující:

```python
oblibenaCisla = (0, 13, 17, 9, 3, 7, -111)
print("je druha mocnina oblibeneho cisla taky oblibene cislo? Zkusime:")
for x in oblibenaCisla: # postupne vezme kazde cislo v oblibenaCisla, ulozi jej do `x` a provede prikazy v bloku cyklu po dvojtecce
    a = x ** 2 # umocni cislo na druhou
    print("z", x, "je", a)
```

---
Úkol2: Udělejte hádankovou hru.
Program si myslí nějaké slovo.
V každém kole dá nápovědu a pak se zeptá uživatele na řešení, pokud uživatelka neuhádne, jde program do dalšího kola.
Bude se vám hodit tuple, for loop a break.
Řešení [zde](ukol2.py).

### Seznamy / List

Datový typ list je velmi podobný Ntici - jde o uspořádanou posloupnost, jeho prvky jsou ale modifikovatelné.
Aby šlo rozlišit list od tuplu, tak list/seznam zadáváme do hranatých závorek, naoplátku jej python vypisuje také v hranatých závorkách:

```python
seznam = ["nula", "jedna", 2, 3, "čtyři", 5.0]
print(seznam) # python seznam vypise v hranatych zavorkach: ["nula", "jedna", 2, 3, "čtyři", 5.0]
```
#### Přístup k prvkům v seznamu

Stejně jako u tuple můžeme přistupovat k prvkům dle jejich pořadí:

```python
seznam = ["nula", "jedna", 2, 3, "čtyři", 5.0]
print(seznam[3]) # 3
print(seznam[0]) # "nula"
print(seznam[5]) # 5.0
```

#### Změna prvků v seznamu

Prvky v seznamu můžeme měnit.
Novou hodnotu do prvku seznamu vložíme stejně jako do obyčejné proměnné, ale navíc do hranatých závorek uvedeme číslo indexu prvku, který chceme měnit:

```python
seznam = ["nula", "jedna", 2, 3, "čtyři", 5.0]
seznam[2] = "dva" # do tretiho prvku / do prvku s indexem dva ulozime retezec "dva", vse je OK, protoze jde o seznam
print(seznam) # vypise: ["nula", "jedna", "dva", 3, "čtyři", 5.0]

# nesmime ale zapomenou uvest index prvku:
seznam = "dva" # zde do cele promenne seznam, v niz je az doposud seznam, ulozime novou hodnotu - retezec "dva"
# nadale uz nejde o seznam, ale o retezec
print(seznam) # vypise: "dva"
```

#### Vkládání nových prvků do seznamu

Ke vkládání prvků do seznamu můžeme použít metodu `append()`, případně metodu `insert()`.
Metoda `append()` vloží daný prvek na konec seznamy:

```python
dochazka = ["Lidmila", "Kristián", "Jilja"]

dochazka.append("Jenovéfa") # pozdni prichod, ale i tak pridame do dochazky

print("lide na vyuce:", dochazka)
```

Pokud chceme vložit prvek na konkrétní místo - i začátek, tak musíme použít metodu `insert()` - její první argument je pozice/index a druhý argument je vkládaný prvek:

```python
todo = ["úkol do angličtiny", "protest na podporu Rojavy", "klauzury"]
todo.insert(1, "hospoda") # na druhou pozici vložíme nový prvek "hospoda" (po práci je třeba se odměňovat)

print(todo) # vypíše: ["úkol do angličtiny", "hospoda", "protest na podporu Rojavy", "klauzury"]
```

#### Vyjímání prvků ze seznamu

Pokud chceme nějaký prvek odstranit ze seznamu, můžeme použít metodu `pop()`, případně klíčové slovo `del`.

```python
hadriky = ["kravata ze sekace", "kravata po babicce", "popalena kravata", "kravata upatlana montazni penou"]
hadriky.pop() # zmensujeme satnik - pop() odstrani posledni vec ze seznamu - v tomto pripade tu nejmin cool
print(hadriky) # vypise: ['kravata ze sekace', 'kravata po babicce', 'popalena kravata']

del hadriky[1] # odstranime druhy prvek v seznamu - darovan blizkemu cloveku
print(hadriky) # vypise: ['kravata ze sekace', 'popalena kravata']
```

---
Úkol3: Vytvořte kombinátor slov/jmen obsažených ve dvou seznamech.
Výsledek ukládejte do seznamy a na konci programu jej vypiště.
Budou se hodit dva plne seznamy, jeden prazdny seznam a for loop.
Řešení [zde](ukol3.py).

## Množiny

Množiny jsou narozdíl od posloupností neseřazené kolekce - prvky nemají určené pořadí.
Množiny podporují operátor příslušnosti `in`, funkci pro zjištění velikosti množiny `len()` a jsou iterovatelné.
Při iteraci vracejí své jednotlivé prvky v náhodném pořadí.

Množiny jsou v Pythonu značeny a vytvářeno pomocí složených závorek:

```python
mnozina = {0, 2, 4, 6, 8, 10}
print(mnozina)
```

Hlouběji se množinám nebudeme věnovat.
