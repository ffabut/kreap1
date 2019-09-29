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
2. VSTUP - program často zpracovává externí informace, jde o možnost jak měnit parametry programy po tom,co jsme jej spustili:
   1. vstup uživatele skrze příkazovou řádku
   2. textové či obrázkové soubory
   3. data z databáze
   4. vstup uživatele skrz webové rozhraní - HTML formuláře atd.
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

Můžeme vypisovat i celá a desetinná čísla, či výsledky matematických operací:

```python
print(12)
print(0.9)
print(2+0.5)
```

---
Všimněme si:
- čísla nepíšeme v uvozovkách
- jaký je rozdíl mezi: `print("15")` a `print(15)`?

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
- jménem proměnné nesmí být klíčové slovo (if, elif, while, for, in a další), není dobré jim dávat ani jména standardních funkcí (print, input a podobně)

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

## Funkce Input (vstup)

## Chybové hlášky

## Proměnné, Porovnávání, Logické operátory: nebo, a, negace