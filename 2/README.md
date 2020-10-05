# Lekce 2

## Python - interpretovaný jazyk

Python je interpretovaný programovací jazyk - primárně tak neslouží k tvorbě spustitelných programů (.exe apod.) jako v případě kompilovaných jazyků (C,C++,Go), ale ke "čtení" - interpretování kódu.
Na počítači, na kterém chceme spouštět python skripty/programy, je tak potřeba mít nainstalovaný Python.
Python čte skript řádek po řádku - definice funkcí (rozebereme později) musí předcházet jejich volání (použití).

Výhody:
- stejný skript můžeme spustit na Windows, Mac i Linux a to bez úprav (v 99% případů)
- instalace Pythonu je jednoduchá a tak spuštění na jiných počítačích či OS není složitá - portabilita kódu. Můžeme psát náš webserver na svém Windows notebooku a pak jej nasadit do produkce na velkém stabilním Linux serveru
- skript hned běží, není třeba trávit čas kompilací
- Python umožňuje interaktivní mód - můžeme ho tak využít k live-codingu apod. Spustíme buď přes IDLE - jde o první okno, které IDLE otevře, tak z příkazové řádky zavoláním příkazu Python bez dalších parametrů (jména souboru k spuštění): `python` případně `python3`. 

Nevýhody:
- pokud chceme, aby někdo používal naše python programy, musí si nainstalovat Python (lze obejít použitím několik knihoven, které umožňují kompilace do spustitelných souborů, např. http://py2exe.org/)
- některé chyby by kompilátor objevil při kompilaci, Python je však objeví až v okamžiku, kdy k nim dojde

## Obecně - co je program?

Zkusme se zamyslet nad tím, co je program?
Jaké má program vlastnosti, co umí?

1. VÝSTUP - většina programů má určitý výstup pro své výsledky, bez výstupu bychom si nebyli jistí, zda program vůbec běží:
   1. vypisuje text do příkazové řádky
   2. upravuje text v souborech
   3. maže soubory
   4. zobrazuje grafiku či webové stránky
   5. return code - číselná hodnota, která řekne, zda program doběhl v pořádku nebo nikoliv
2. VSTUP - program často zpracovává externí informace, jde o možnost jak měnit parametry programy po tom, co jsme jej spustili:
   1. vstup uživatele skrze příkazovou řádku
   2. textové či obrázkové soubory
   3. data z databáze
   4. data z webu
   5. vstup uživatele skrz webové rozhraní - HTML formuláře atd.
3. UKLÁDÁNÍ DAT - program si potřebuje "pamatovat" určité informace během svého běhu, může jít o:
   1. proměnné - dočasné uložiště platné během běhu programu, nebo jen v určitých jeho částech
   2. trvalejší úložiště - databáze, konfigurační soubory apod.
4. ŘÍZENÍ BĚHU PROGRAMU - občas je důležité běh programu rozvětvit, reagovat na nastalé situace rozdílnými akcemi:
   1. podmínky - IF-ELSE-ELIF
   2. cykly - WHILE, FOR - slouží k opakování určitého úkonu dokud nejsou splněny podmínky

Pokud se naučíme alespoň základ z každého ze 4 odvětví, budeme schopné a schopní psát relativně fungující a plnohodnotné skripty/programy.
Pojďme na to.

## Jak vytvořit Python skript

Postup pro vytvoření skriptu je následující:
1. otevřít IDLE, případně http://repl.it
2. skrze ně vytvořit nový soubor `main.py`
3. napsat kód a uložit jej
4. spustit kód
   1. v IDLE - v menu záložka `Run - Run Module`, případně klávesou F5
   2. v repl.it - tlačítko `Run`

Alternativně lze python kód psát v libovolném textovém editoru bez formátování (poznámkový blok, nano, vim, emacs apod.) a poté jej spouštět z příkazové řádky (PowerShell na Windows, Terminal na Mac a Linux) za použití příkazu `python` či `python3`.
Pythonový kód - skript uložený v souboru main.py můžeme spustit příkazem:

```
python3 main.py
```

---

Poznámka: je možné a leckdy i žádoucí skript pojmenovat i jinak než `main.py`, například `mujserver.py` či `sendmail.py`.
V případě, že píšeme složitější projekt, je zvykem, že `main.py` je určitým vstupním, prvotním skriptem, který importuje všechny ostatní.

---

Poznámka 2: koncovka `.py` není nutná.
Často se objevuje i koncovka `.py3` značící, že jde o skript v Pythonu 3, případě `.pyw` u GUI aplikací.
Koncovky jde i kompletně vynechat, či použít jiné, ale je dobrým zvykem používat právě `.py` nebo `.py3` a to z důvodu čitelnosti a srozumitelnosti.

## První program Hello World

Tredičně je prvním programem jisté pozdravení světa do textového výstupu.
V Pythonu jde o jeden řádek používající standardní funkci `print()` (standardní ve smyslu, že je standardní součástí jazyka Python, není ji třeba nijak doinstalovávat či definovat jako novou vlastní funkci, je dostupná vždy). K pozdravení zavoláme funkci print s parametrem pozdravu, následovně:

```python
print("Hello, world!")
```

Celý skript zde: [1/hello-world.py](hello-world.py).

---
Všimněme si:
- pozdrav jakožto text je psán v uvozovkách (dvojice jednoduchých '' či složených "") - bez nich by python nepoznal, že myslíme text/textový řetězec a nikoliv třeba další kód

## Funkce Print (výstup)

Funkce print(), kterou jsme před chvílí použili je jednou z nejpraktičtějších funkcí - s ní můžeme komunikovat s uživatelem, ale i vypisovat určité hodnoty během běhu programu a zjišťovat tak, zda vše běží jak má, nebo hledat, kde máme chybu - debugovat.

Funkci print můžeme volat i s více parametry (hodnotami v závorce oddělených čárkou):

```python
print("Ahoj,", "světe!", "(česky)")
```

Nebo můžeme volat print bez parametru:

```python
print()
```

V tomto případě funkce `print()` vytiskne pouze prázdný řádek.
Všimněme si také, že jsou stále potřeba závorky za jménem funkce - závorky Pythonu říkají, že jde o volání funkce.

Pomocí funkce `print()` můžeme vypisovat nejen textové řetězce, ale i celá a desetinná čísla, hodnoty True/False a mnoho dalších - a navzájem je kombinovat (není třeba mít všechny parametry stejného typu).
Funkce `print()` zvládne defacto vypsat téměř vše, co do ní pošleme.
Můžeme jako parametr do funkce `print()` poslat i samotnou funkci print (bez závorek, aby nešlo o volání funkce, ale o funkci jako objekt.)

```python
print(12)
print(0.9)
print(True)
print(print)
print(12, 0.9, True, "Ahoj", print)
```

Poznámka: chceme-li vyjádřit čísla, nepíšeme je v uvozovkách.
S uvozovkami by je python vyhodnotil jako řetězce.

---
Otázky:
- jaký je rozdíl mezi: `print("15")` a `print(15)`?

## Komentáře a čitelnost

Kód neslouží pouze k udávání povelů počítači, je často také čten lidmi - jinými programátorkami a programátory i námi samotnými někdy v budoucnu.
Je proto dobré udržovat kód čitelný a jasný.
Mezi dobré praktiky slouží smyslyplné pojmenovávání proměnných a funkcí (co jsou proměnné a funkce si vysvětlíme později).

Mezi klíčové nástroje pro čitelnost ale patří především komentáře.
Jde o úseky v kódu, které neovlivňují chod programu - jsou Pythonem či jinými jazyky ignorovány - a slouží pouze ke čtení lidmi.
Komentáře v Pythonu začínají křížkem/hashtagem #, vše na řádku za tímto znakem je ignorováno:

```python
# Tady pozdravíme svět
print("Ahoj, světe!")

print("Ahoj, FaVU!") # A tady zdravíme FaVU
```

Více-řádkové komentáře v Pythonu neexistují, což je trochu nepraktické.
Funkci více-řádkového komentáře, ale můžeme nahradit pomocí více-řádkového textového řetězce, který neuložíme do žádné proměnné.
Python tak takový řetězec bude ignorovat.
Příklad:

```python
retezec = """
Toto je viceradkovy retezec,
ktery jsme ulozili do promenne 'retezec'.
python tak tento retezec neignoruje, ale zpracovava
"""

"""
a toho je viceradkovy retezec,
ktery do zadne promenne neukladame
a tak ho python totalne ignoruje
defacto jde o viceradkovy komentar
"""

```

## Proměnné (ukládání dat)

Občas je vhodné si výsledek či hodnotu "uložit".
K tomuto účelu slouží v programování proměnné.
V Pythonu narozdíl od některých jazyků nemusíme předem definovat, jaký typ dat do proměnné uložíme (textový řetězec, celé číslo, desetinné apod.).
Jednoduše napíšeme název proměnné a pak jí přiřadíme hodnotu pomocí znaménka rovná-se =.
Hodnota vpravo se ukládá do hodnoty vlevo, například:

```python
jedna = 1
dva = 2
print(jedna + dva)

print("jedna" + "dva")
```

Všimněme si:
- jména proměnných nepíšeme do uvozovek (python by je bral jako obyčejný textový řetězec)
- jménem proměnné nesmí být klíčové slovo (if, elif, while, for, in a další), není dobré jim dávat ani jména standardních funkcí (print, input a podobně) a datových typů (int, str, bool)- pak bychom si tyto funkce či datové typy "přepsali" novou hodnotou a už bychom je dál v programu nemohli používat...

Dále platí, že jména proměnných:
- musí začínat písmenem, nebo podtržítkem
- nesmí začínat číslicí
- jsou case-sensitive, je rozdíl mezi `user1`, `USER1`, `User1`

---

Obsah proměnné můžeme měnit, dokonce můžeme měnit datový typ, který je v proměnné uložen:

```python
rocnik = 1
rocnik = 2
rocnik = "treti"
rocnik = 4.0
rocnik = "nmgr-1"
print(rocnik)
```

Do proměnné můžeme přiřadit hodnotu jiné proměnné:

```python
Prijmeni = "Ondrackova"
prijmeni = Prijmeni

jmeno = "Pavla"
celeJmeno = jmeno + prijimeni
print(celeJmeno)
```

Všimněme si, že:
- můžeme "sčítat" textové řetězce
- proměnné je dobré pojmenovávat smysluplnými názvy, aby bylo jasné, co je v proměnné uloženo - ušetříme si tím starosti, až po sobě budeme číst kód někdy v budoucnu, případně pokud jej bude číst někdo další

Pozor: nemůžeme používat proměnou před tím, než do ní uložíme hodnotu.
Python by v takové případě nevěděl, jaká je její hodnota - mělo by to být 0, prázdný řetězec "", False, None či jaká hodnota?

```python
a = 10
print(a + b) #zde dojde k chybě
```

Pokud tento kód zkusíme spustit, vyskočí na nás chybová hláška: `NameError: name 'b' is not defined`.

### Datové typy

Proměnné mohou obsahovat různé typy dat - zatím jsme se setkali s textovými řetězci, celými a desetinnými čísly.
Můžeme použít ale i logický typ tzv. Boolean (true/false) a mnoho dalších.
Pokud si nejsme jistí, jaký datový typ proměnná obsahuje, můžeme použít funkci `type()`:

```python
jmeno = "Adam"
vek = 26
energie = 0.34
happy = True

print(type(jmeno))
print(type(vek))
print(type(energie))
print(type(happy))
```

Těch základních datových typů však mnoho není:

#### integer (zkráceně int) - celá čísla

S integer (celými čísly) můžeme provádět všechny očekávatelné matematické operace, základními jsou:

```python
# sčítání - výsledek je celé číslo
soucet = 5 + 1
print(soucet)


# odčítání - výsledek je celé číslo
rozdil = 9 - a
print(rozdil)


# násobení - výsledek je celé číslo
soucin = a * b
print(soucin)


# dělení - pozor: výsledkem dělení je v Pythonu 3 datový typ float
podil = 10 / 3
print(podil)

# float je výsledkem dělení, i když vyjde celé číslo
print(type(soucet))
print(type(rozdil))
print(type(soucin))
print(type(podil))
print(type(10/2))
```

Mezi další operace patří:

```python
# celociselne deleni - zaokrouhleny podil - vysledek je cele cislo
podil = 10 // 3
print(podil)

# tzv. modulo - zbytek po celociselnem deleni - vysledek je cele cislo
# hodi se, pokud chceme provadet nejaky ukon v kazdem druhem, tretim, desatem pripade a podobne...
zbytek = 10 % 3
print(zbytek)
print(11 % 3)
print(12 % 3)
print(13 % 3)

# mocnina - vysledek je cele cislo
squared = 2 ** 3
print(squared)
print(5 ** 2)
print(5 ** 3)
```

#### float (float) - čísla pohyblivou desetinnou čárkou

Float neboli čísla s pohyblivou čárkou jsou defacto desetinná čísla.
(Python má však i speciální typ `decimal` s vyšší přesností a proto mluvíme o float trochu neintuitivně jako číslech s pohyblivou desetinnou čárkou a ne přímo o desetinných číslech.)
Float může být v určitých situacích mírně nepřesný - dělení drobných extrémně malých čísel, v běžném užití to ale nemusíme příliš řešit.
Pokud bychom dělali přesné fyzikální či bankovní výpočty, je ale lepší se podívat a použít přímo `decimal`.

Chceme-li v Pythonu vytvořit proměnnou jako typ `float`, zadáme hodnotu proměnné jako číslo s desetinnou čárkou (zapsanou anglickým způsobem znakem tečky) - Python na oplátku desetinná čísla vždy vypisuje také s tečkou:

```python
f = 0.5

# pokud jde o celé číslo, které ale chceme mít jako float, také použijeme tečku
f = 7.0 # toto je float

i = 7   # toto je integer

print(10.0 / 2.0) # i když by výsledek mohl být celé číslo, Python jej vypíše s tečkou, protože jde o typ float 
```

Float umožňuje stejné operace jako integer, výsledek je vždy opět float:

```python
print(10.0 + 1.0) # sčítání - výsledek je float
print(10.0 - 1.0) # odčítání - výsledek je float
print(10.0 * 2.0) # násobení - výsledek je float
print(10.0 / 3.0) # dělení - výsledek je float
print(10.0 // 3.0) # celočíselné dělení - pozor výsledek je stejně float
print(10.0 % 3.0) # zbytek po dělení - pozor výsledek je stejně float
print(10.0 ** 2.0) # mocnina - výsledek je float
```

##### Interakce float a integer

Pythonu nevadí, pokud chceme dělat operace nad float a integer zaráz, umí si s tím poradit.
Matematické operace tak jsou intuitivní, vše se chová podobně jako v normálním světě, kde také dokážeme v pohodě sečíst 10 a 5.5, případně 10.5 a 5.
Pokud se ve výpočtu objeví alespoň jeden float, je výsledek vždy float:

```python
print(10.0 + 1) # sčítání - výsledek je float
print(10 - 1.0) # odčítání - výsledek je float
print(10 * 2.0) # násobení - výsledek je float
print(10.0 / 3) # dělení - výsledek je float
print(10.0 // 3) # celočíselné dělení - pozor výsledek je stejně float
print(10 % 3.0) # zbytek po dělení - pozor výsledek je stejně float
print(10 ** 2.0) # mocnina - výsledek je float
```

#### string (zkráceně str) - textové řetězce

Typ string neboli textový řetězec slouží k ukládání textu.
Píšeme jej vždy do uvozovek, Python by si jinak mohl řetězec splést se jménem proměnné či jiným klíčovým slovem:

```python
jmeno = "Daliborka" # do proměnné jmeno uložíme textový řetězec "Daliborka" 
preferovaneOsloveni = Daliborka # do proměnné preferovaneOsloveni ulozime hodnotu promenne Daliborka - ta ale nebyla zatim definovana a tak dojde k chybe
```

K hlubší podstatě, háčkům a vychytávkám textových řetězců se vrátíme později.
Prozatím nám bude stačit pár základních operací se string:

```python
jmeno = "Marie"
prijmeni = "Malinová"

# sčítání - či spíše spojování řetězců
celeJmeno = jmeno + prijmeni
print(cele jmeno)

# násobení řetězců
jmenoStokrat = jmeno * 100
print(jmenoStokrat)
```

---
**Úkol:**

- Jak sečíst jméno a příjmení, aby mezi nimi byla mezera?

```{python echo=FALSE}
jmeno = "Marie"
prijmeni = "Malinová"

# do scitani muzeme pridat textovy retezec obsahujici mezeru: " "
celeJmeno = jmeno + " " + prijmeni
```
---

Další operace jako dělení, odčítání, mocnina a podobně nejsou se string možné.
I v reálném životě bychom si je těžko představovali.
Jaký by měl být výsledek `"Petr"/2`?
Těžko říct. A tak Python tyto operace nemá.

#### boolean (zkráceně bool) - logické hodnoty True/False

Typ boolean je logickým typem, může mít pouze dvě hodnoty - `True` nebo `False`.
Boolean se hodí v případě, kdy chceme řídit tok programu a vyhovět několika podmínkám zaráz.
Zadala uživatelka jméno A zadala email NEBO telefon?
Základní operace s booleanem jsou definovány klíčovými slovy `and`, `or`  a `not`:

```python
# AND - výsledek je True, jen pokud jsou obě hodnoty True
print(True and True) # =True
print(True and False) # =False
print(False and True) # =False
print(False and False) # =False

# OR - výsledek je True, pakliže alespoň jedna hodnota je True, případně obě jsou True

print(True or True) # =True
print(True or False) # =True
print(False or True) # =True
print(False or False) # =False

# NOT - neguje následující booleanovskou hodnotu
print(not True) # =False
print(not False) # =True
```

---
**Tip:**

Hodnota True v Pythonu odpovídá také hodnotě 1, hodnota False odpovídá také hodnotě 0.
Teoreticky můžeme dělat operace jako `1 + True`, což by se rovnalo 2.
V praxi je to ale zbytečné.
Nachytat by nás ale mohlo porovnávání `1 == True`, které je pravdivé, True se skutečně rovná 1, více v kapitole porovnávání hodnot.

---

#### NoneType

NoneType je speciálním typem, který má pouze jednu hodnotu a tou je `None`, jeho významem je čisté nic - ani 0, ani False, ani prázdný řetězec, ale nic - `None`.
Užívá se například v situaci, kdy chceme informovat o chybách - pokud se něco pokazí, vrátíme chybu, pokud vše proběhne v pořádku, vrátíme hodnotu `None`.
Více toho k `None` snad ani není a tak se jen později dostaneme k tomu, že na něj narazíme a začneme ho používat. 


### Porovnávání hodnot

Často se dostaneme do situace, kdy budeme chtít porovnat dvě různé hodnoty.

#### Rovná se / Nerovná se

Základní provnáním je rovná se `==`, případně nerovná se `!=`.
Všimněme si, že klasické "rovná se" se v Pythonu i dalších jazycích píše dvěmi rovnítky, zatímco klasické rovná se má význam přiřazení - do proměnné vlevo přiřadí hodnotu napravo a nejde tedy o porovnávání.
Výsledkem porovnání je typ Boolean, tedy hodnoty `True` nebo `False`:

```python
# rovná se
print(7 == 7) # =True
print(7 == 10) # =False

# nerovná se
print(7 != 7) # =False
print(7 != 10) # =True

a = 8
b = 9
a = b # do proměnné a přiřadí hodnotu proměnné b - nevrací True ani False, nejde o porovnávání, ale o přiřazení hodnoty 
```

Porovnávat ale můžeme i jiné typy, například string, float, boolean nebo NoneType:

```python
print("Ahoj" == "Ahoj") # =True
print(True == True) # =True
print(8.001 == 8.001) # =True

print("Ahoj" != "Hi") # =True
print(True != False) # =True
print(8.0000000001 != 8.000000002) # =True
```

Pomocí `==` a `!=` můžeme dokonce porovnávat dva zcela odlišné typy:

```python
print("Ahoj" == 7) # =False
print(True == 90) # =False
print(12 == None) # =False

print(8.0 == 8) # =True
print(True == 1) # =True - True mimojiné odpovídá hodnotě 1, toto je trochu chyták
print(False == 0) # =True - False mimojiné odpovídá hodnotě 0, trochu chyták
```

#### Větší / Menší / Větší nebo rovno / Menší nebo rovno

Číselné typy můžeme porovnávat i pomocí operací větší než, menší než, větši nebo rovno, menší nebo rovno:

```python
# > větší než
print(5 > 1) # =True
print(1 > 5) # =False

# < menší než
print(5.0 < 10.0) # =True
print(9.9 < 9.8) # =False

# >= větši nebo rovno
print(5.0 >= 1) # =True
print(5.0 >= 5) # =True
print(5.0 >= 5.1) # =False
print(5 >= 5.1) # =False

# <= menší nebo rovno
print(5.0 <= 10) # =True
print(5.0 <= 5) # =True
print(5.0 <= 1) # =False
print(5 <= 1.0) # =False
```

---
**Pozor**

Větší/menší můžeme použít i pro porovnání délky textových řetězců.
Nelze však porovnávat například textový řetězec a číslo. 

---

### Prevody datovych typu 

Občas je potřeba překonvertovat jeden datový typ do jiného, například převést řetězec `"2019"` na celé číslo.
K těmto účelům slouží standardní funkce `int()`, `float()` a `str()`:

```python
cislo = 2019
rok = "2019"
desetinne = 2019.5

a = str(cislo)
b = str(desetinne)

print(type(a)) # z int cisla 2019 je nyni retezec "2019"
print(type(b)) # z float cisla 2019.5 je nyni retezec "2019.5"


```

## Funkce Input (vstup)

Potřebujeme-li získat vstup od uživatele skrze příkazovou řádku, můžeme v Pythonu použít funkci `input()`.
Tato funkce nepotřebuje žádné parametry (hodnoty v závorce), avšak i tak jsou tyto prázdné závorky potřeba.
Vysvětlení a více o funkcích bude rozebráno později.

Narozdíl of funkce `print()`, který vypisuje do příkazové řádky, funkce `input()` vrací hodnoty - text zadaný uživatelkou.
Jak se k němu můžeme dostat?
Jednoduše přiřadíme tuto navrácenou hodnotu do proměnné.
V praxi to pak vypadá takto:

```python
# zavolame funkci input() a jeji navracenou hodnotu priradime do promenne textUzivatele
textUzivatele = input()

# zadany text ulozeny do promenne textUzivatele pak muzeme treba vypsat zpet do prikazove radky
print("zadala jsi text:", textUzivatele)
```

Celou situaci si můžeme představit tak, že navrácená hodnota funkce nahradí funkci na jejím původním místě, například:

```python
a = input()
#je vlastne:
a = "zadany text"
```

## Úkol 1

Vytvořte program, který:
- uživatelku poprosí o zadání jejího jména 
- a pak ji tímto jménem osloví

### Řešení

- [interactive-hello.py](interactive-hello.py)  
- [interactive-hello-alternative.py](interactive-hello-alternative.py)

## Úkol 2

Vytvořte program, který pomůže s nějakou početní operací.
Například:
- zobrazení součtu, rozdílu, násobku a podílu dvou zadaných čísel (výsledek: [4cisla.py](4cisla.py))
- počítadlo peněz za brigádu (výsledek: [brigada.py](brigada.py))
- odhad plochy místnosti kvůli nákupu primalexu na instalaci výstavy
- výpis zadaného jména tolikrát, kolikrát si uživatelka přeje3

### Řešení

- 
- [interactive-hello2.py](interactive-hello2.py)