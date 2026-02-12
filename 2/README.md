# Lekce 2

## Stručná historie programovacích jazyků

Počítače ve své podstatě rozumí pouze velmi jednoduchým instrukcím ve formě strojového (binárního) kódu — tedy posloupnostem nul a jedniček.
Tento kód je závislý na konkrétní architektuře procesoru (CPU) a často také na operačním systému, protože využívá jeho služby (práce se soubory, okna, síť apod.).
Psát programy pro počítače přímo ve strojovém kódu je tak pro člověka extrémně složité.
V počátcích výpočetní techniky v 40. a 50. letech se však takto psalo, a to i poměrně složité programy, jelikož zkrátka nebylo na výběr.

Between 1942 and 1945, Konrad Zuse developed Plankalkül ("plan calculus"), the first high-level language for a computer, for which he envisioned a Planfertigungsgerät ("plan assembly device"), which would automatically translate the mathematical formulation of a program into machine-readable punched film stock.[1] However, the first actual compiler for the language was implemented only decades later. 

Souběžně s tím se však objevovaly snahy tento proces zjednošit.
Mezi lety 1942 a 1945 Konrad Zuse přišel v nacistickém Německu s konceptem jazyka Plankalkül ("plan calculus"), prvního high-level programovací jazyk pro počítač, plánovaného pro jeho počítače Z3 a později Z4.
Pro něj si představoval Planfertigungsgerät ("plan assembly device"), který by automaticky překládal matematické formulace programu do strojově čitelného děrovaného filmového pásu.
Implementace tohoto konceptu však přišla až v roce 2000, kdy byl vytvořen Plankalkül-Compiler v rámci projektu na FU Berlin.

Autorkou prvního reálně implementovaného kompilátoru/překladače byla americká počítačová vědkyně a matematička Grace Hopper, jež mezi lety 1951 a 1952 napsala její kompilátor "A-0 system" pro počítač ENIAC.
Současně s tím také zavedla samotný termín "compiler" - česky kompilátor či překladač.
Její koncepce překladače, který umožňoval psát kód v srozumitelnější formě, která byla pro člověka snazší na psaní i čtení, a následně tento lidský kód překládal do strojového kódu, kterému počítač rozumí, se ukázal jako fungující. 
Kompilátory od té doby můžeme vnímat jako překladatele mezi lidskou řečí a strojovým kódem.

Forma překladu se však velmi liší na základě konkrétního programovacího jazyka, jeho filozofie, účelu i historického kontextu, ve kterém vznikl.
Jedním z nejstarších jazyků s kompilátorem je Assembler, který vznikl v 50. letech 20. století a umožňoval psát kód pomocí krátkých textových instrukcí místo čísel.
Byl velkým krokem vpřed k čitelnosti, ale z dnešního hlediska má stále velmi blízko k hardwaru a programování v něm je náročné a zdlouhavé.
Odvážné osoby si mohou rozkliknout [Hello World v assembleru](https://www.itnetwork.cz/assembler/zaklady/assembler-prvni-program-hello-world).

Postupem času docházelo jak k vývoji ve filozofii a designu programovacích jazyků (paradigmata procedurální vs. objektově orientované vs. funkcionální), tak v míře, v níž tyto jazyky abstrahují nad samotným hardwarem.
Nejníže si můžeme představit samotný strojový kód, nad nímž stojí Assembler, který je stále velmi blízko hardwaru, ale už nám umožňuje používat textové instrukce.
Nad ním můžeme vidět jazyk C, který je stále poměrně blízko hardwaru, ale už nám umožňuje používat složitější datové struktury a abstrakce.
Nad ním stojí jazyk C++ nebo C#, který přidává objektově orientované paradigma, a nad ním jazyk Java, který přidává další abstrakce a je navržen pro běh na virtuálním stroji (JVM), což zvyšuje jeho přenositelnost mezi různými platformami.
Jazyk Python, který se objevil v roce 1991, je navržen pro jednoduchost a čitelnost, a je vysokoúrovňový jazyk, který abstrahuje od hardwaru a operačního systému.

Jazyky s vyšší úrovní abstrakce nám umožňují psát kód rychleji a s menší pravděpodobností chyb, ale mohou být pomalejší než jazyky s nižší úrovní abstrakce, protože přidávají další vrstvy mezi námi a hardwarem.
A také nám berou absolutní kontrolu nad tím, co se děje "pod kapotou", což může být nevýhodné pro některé typy aplikací, jako jsou operační systémy, hry nebo jiné výkonnostně velmi velmi náročné programy, či naopak programy na omezených zařízeních, jako jsou mikrokontroléry.

### Kompilované vs. interpretované jazyky

Pokud vše začalo strojovým kódem a pokračovalo kompilátory, tak další vývojovou fází jsou poté takzvané interpretované jazyky, které fungují trochu jinak.
Interpretované jazyky fungují trochu jinak: namísto kompilátoru, který vytváří spustitelný programu, mají interpretované jazyky interpret - což je vlastně program, který čte běžný text a na základě jeho interpretace vykonává požadované úkony, operace.

Interpret je sám o sobě běžný program, který je přeložený do strojového kódu stejně jako jiné aplikace (typicky pomocí kompilátoru).
Jakmile však tento interpret máme nainstalovaný, můžeme v něm spouštět libovolné programy napsané v jeho jazyce, aniž bychom je museli pokaždé znovu kompilovat.

Trochu paradoxní je, že interpret je program, který je často napsaný a zkompilovaný v kompilovaném jazyce.
Python má základní interpret (zvaný CPython) napsaný v C, který je zkompilovaný do strojového kódu, a tento interpret nám umožňuje spouštět Pythoní kód.
Vývojářstvo Pythonu kompiluje CPython na řadu operačních systémů a architektur, takže můžeme spouštět Pythoní kód na Windows, Mac i Linuxu bez úprav.

## Python - interpretovaný jazyk

Python je interpretovaný programovací jazyk - primárně tak neslouží k tvorbě spustitelných programů (.exe apod.) skrze kompilátor - jako v případě kompilovaných jazyků (C, C++, Go, Arduino).
Namísto toho Python interpret při spuštění program postupně čte kód řádek po řádku a vykonává jednotlivé instrukce.

Proto je na každém počítači, kde chceme Python program spustit, potřeba mít Python nainstalovaný — tedy právě tento interpret.
Python obvykle vykonává kód řádek po řádku.
To například znamená, že definice funkcí (které si vysvětlíme později) musí být uvedeny dříve, než je zavoláme, použijeme.
(Kompilátory naproti tomu přečtou celý kód a teprve potom vytvářejí samotný překlad - překlad knihy vs. hraní z not na první dobrou.)

Výhody interpretovaných jazyků:
- stejný skript můžeme spustit na Windows, Mac i Linux a to bez úprav (v 99% případů)
- instalace Pythonu je jednoduchá a tak spuštění na jiných počítačích či OS není složitá - portabilita kódu. Můžeme psát náš webserver na svém Windows notebooku a pak jej nasadit do produkce na velkém stabilním Linux serveru
- skript hned běží, není třeba trávit čas kompilací
- Python umožňuje interaktivní mód - můžeme ho tak využít k live-codingu apod. Spustíme buď přes IDLE - jde o první okno, které IDLE otevře, tak z příkazové řádky zavoláním příkazu Python bez dalších parametrů (jména souboru k spuštění): `python` případně `python3`. 
- náš program můžeme klidně poslat SMSkou nebo dopisem, jde totiž o prostý text

Nevýhody:
- pokud chceme, aby někdo používal naše python programy, musí si nainstalovat Python (lze obejít použitím několik knihoven, které umožňují kompilace do spustitelných souborů, např. http://py2exe.org/)
- některé chyby, co uděláme, by kompilátor objevil při kompilaci, Python je však objeví až v okamžiku, kdy k nim dojde - což může být v nevhodnou chvíli

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
2. skrze ně vytvořit nový soubor, např.: `main.py`
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
V případě, že píšeme složitější projekt, je zvykem, že `main.py` (případně název našeho projektu tečka py) je určitým vstupním, prvotním skriptem, který importuje všechny ostatní.

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

Celý skript zde: [hello-world.py](hello-world.py).

---
Všimněme si:
- pozdrav jakožto text je psán v uvozovkách (dvojice jednoduchých '' či složených "") - bez nich by python nepoznal, že myslíme text/textový řetězec a nikoliv třeba další kód

---
Úkol: Upravte Hello World tak, aby vypsal pozdrav na dva řádky, na druhém řádku byl text: "Welcome to Python!"
Můžeme volat funkci dvakrát po sobě?

Řešení: [hello-world-and-welcome.py](hello-world-and-welcome.py)

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

---

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

Úkol: Vypište pomocí jedné funkce print() své jméno, věk a město, věk zadejte jako číslo nikoliv jako součást textového řetězce, například: `Ahoj, jmenuji se Nikola, je mi 28 let a bydlím v Praze.`
Zkuste nepoužívat jeden dlouhý řetězec, ani spojování řetězců pomocí +, ale více parametrů oddělených čárkou.

Řešení: [print-multiple-params.py](print-multiple-params.py)

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

### Docstrings
Docstrings neboli dokumentační řetězce - jsou komentáře ve speciálním formátu, který IDLE a jiné IDEs (integrated development environment) rozpoznají a zapracují do svého grafického rozhraní.
Funkce a třídy okomentované docstring nám pak zobrazí rovnou s docstringem jako mini-návodem, jak funkci nebo objekt použít.

Funkce a třídy můžeme anotovat pomocí více řádkových komentářů za definicí funkce:
```python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...

class Dragon():
   """Třída fantastické bytosti draka. Umí chrlit oheň."""
   def FireBreath(self):
      """Docstring můžou mít i metody (funkce v rámci) třídy."""
      print("Chrlím oheň!")
   ...
```

Více informací o docstrings v [PEP-257](https://peps.python.org/pep-0257/).


## Proměnné (ukládání dat)
Při běhu programu často potřebujeme dočasně uložit data a později se k nim dostat.
K tomuto účelu slouží v programování proměnné.

Proměnná je označení pro identifikátor (symbolické jméno), který uchovává určitou informaci (data) při běhu programu.
Proměnná může nabývat známých nebo neznámých informací, které se nazývají hodnota.
Jméno proměnné je obvyklá cesta k získání reference k hodnotě uložené někde v operační paměti počítače.
Separace jména a obsahu umožňuje použít jméno, které se používá nezávisle na přenesené informaci, kterou zastupuje.

Jelikož je Python dynamicky typovaný, tak narozdíl od jiných staticky typovaných jazyků (např. C, C++, Go, Rust) nemusíme předem definovat, jaký typ dat do proměnné uložíme (textový řetězec, celé číslo, desetinné apod.).
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
- jménem proměnné nesmí být klíčové slovo (if, elif, while, for, in a další)
- jménem proměnné je lepší nedávat ani jména standardních funkcí (print, input a podobně) a datových typů (int, str, bool)- pak bychom si tyto funkce či datové typy "přepsali" novou hodnotou a už bychom je dál v programu nemohli používat...

Dále platí, že jména proměnných:
- musí začínat písmenem, nebo podtržítkem
- nesmí začínat číslicí
- jsou case-sensitive, je rozdíl mezi `user1`, `USER1`, `User1`

---

Obsah proměnné můžeme měnit.
Jelikož je Python dynamicky typovaný programovací jazyk, tak dokonce můžeme měnit datový typ, který je v proměnné uložen:

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
celeJmeno = jmeno + prijmeni
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

<details>
<summary>
Úkol: Zjistěte pomocí operátoru %, zda je číslo dělitelné 24.
</summary>

```python
frames = 127938
zbytek = frames % 24
print("Mame extra", zbytek, "frames, ktere se nevejdou do celých sekund.")
```

</details>

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

<details><summary>řešení</summary>
<p>

```python
jmeno = "Marie"
prijmeni = "Malinová"

# do scitani muzeme pridat textovy retezec obsahujici mezeru: " "
celeJmeno = jmeno + " " + prijmeni
```
</p>
</details>

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

Vytvořte program, který spočítá dlouhodobou spotřebu kávy.

Program:
- zeptá se uživatelestva, kolik šálků kávy (espresso) vypije denně,
- spočítá, kolik šálků vypije za rok,
- spočítá spotřebu za 10 let,
- odhadne, kolik gramů kávy se na tato espressa (7g kafe) spotřebuje,
- spočítá, kolik miligramů čistého kofeinu uživatelstvo za 10 let přijme (espresso ~ 63mg kofeinu).

Řešení: [kafe.py](kafe.py)

## Úkol 3

Vytvořte program, který pomůže s nějakou z následujících početních operací:
- zobrazení součtu, rozdílu, násobku a podílu dvou zadaných čísel (výsledek: [4cisla.py](4cisla.py))
- počítadlo peněz za brigádu (výsledek: [brigada.py](brigada.py))
- odhad plochy místnosti kvůli nákupu primalexu na instalaci výstavy
- výpis zadaného jména tolikrát, kolikrát si uživatelka přeje
