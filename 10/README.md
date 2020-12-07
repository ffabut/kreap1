# Absolutní a relativní cesty

## Cesty

Při programování občas potřebujeme pracovat se soubory - ať již jde o textové soubory pro čtení a zápis, binární soubory, složky, tak například soubory databází (SQLite), nebo různé HTML templaty, CSS a JavaScript soubory, když programujeme webový server.
Aby Python byl schopný soubor najít a dále s ním pracovat, musíme uvést cestu - místo na disku, na němž má Python soubor hledat.
Máme přitom dvě možnosti, jak cestu zadat: jednou je absolutní cesta (uvádí kompletní cestu od disku/rootu až k souboru), druhou poté relativní cesta (uvádí cestu k souboru od složky, z níž jsme spustili Pythonový skript - tzv. working directory).

### Working directory

Working directory je pojem, který označuje cestu k adresáři/složce, z níž jsme spustili skript nebo program.
Jelikož při používání příkazuy `python3`/`python` můžeme spouštět i skript, který je mimo složku, v které se zrovna nacházíme, tak se working directory nemusí krýt s umístěním našeho skriptu.
Příklad:

```
(/home/ja) python3 main.py

>> working directory je: /home/ja
>> a je stejna jako umisteni main.py v /home/ja
```

```
(/home/ja) python3 /mujProjekt/main.py

>> working directory je: /home/ja
>> umisteni main.py je ale jine: /home/ja/mujProjekt
```

Working directory je vždy místo, odkud voláme příkaz `python` - ať už s ním otvíráme skript kdekoliv - na jiném disku, v jiných složkách, nebo přímo v dané složce.

#### Zjištění working directory v Pythonu

Pro zjištění working directory ze skriptu můžeme použít funkci `os.getcwd()` (get current working directory) z built-in modulu `os`:

```python
import os

wd = os.getcwd()
print("working directory je:", wd)
```

#### Změna working directory

Working directory můžeme během běhu programu změnit pomocí funkce `os.chdir()` (change directory) z built-in modulu `os`:

```python
import os

print(os.getcwd()) # bude dost mozna neco jako /home/jmeno, pripadne umisteni, odkud spoustime skript v IDLE

os.chdir("/home") # na windows nebude fungovat, navolte nějakou vlastní cestu, například: `C:/Users`

print(os.getcwd()) # nyni je working directory nastavena na: /home
```

#### Zjištění umístění skriptu

Pokud bychom chtěli zjistit umístění samotného skriptu a nikoli working directory, můžeme použít proměnnou `__file__`, v níž Python uchovává relativní cestu ke skriptu od working directory, a funkci `os.path.realpath()`, pomocí níž z relativní cesty uděláme absolutné cestu:

```python
import os

print(os.getcwd()) #například: /home/ja
print(__file__) # vypíše jméno souboru (např. main.py), případně složky vedoucí k souboru, pokud je soubor mimo working directory
# v našem případě např: skripty/test/main.py

absPath = os.path.realpath(__file__)
print(absPath) # napriklad: /home/ja/skripty/test/main.py

# pokud bychom chtěli jen složku, v níž se main.py nachází, můžeme jméno souboru odstranit pomocí funkce `os.path.dirname()`
# a získat pouze cestu ke složce, v níž se spuštěný skript nachází:

print(os.path.dirname(absPath)) # v našem příkladu např.: /home/ja/skripty/test
```

#### IDLE

Pokud spouštíme skript přes IDLE, tak IDLE automaticky nastaví working directory na složku, v níž máme skript, který spouštíme.
To je velmi praktické, ale je dobré pamatovat na to, že může přijít někdo, kdo bude náš skript spouštět z příkazové řádky z naprosto odlišné složky.
Měli bychom s tím počítat a nespoléhat se na to, že working directory bude vždy shodná se složkou, v níž máme skript.

### Relativní cesta

Relativní cesta uvádí cestu k souboru či složce relativně k working directory, relativní cesta nezačíná lomítkem `/` (na Mac a Linux), případně písmenem disku, dvojtečkou a lomítkem `C:/` (na Windows), ale začíná bez nich, například:

- `main.py` - soubor main.py ve working directory
- `scripts/main.py` - ve working directory se nachází složka scripts a v ní soubor main.py
- `scripts/hacks/10.py` - ve working directory se nachází složka scripts, v ní složka hacks a v ní soubor 10.py

V relativní cestě ale můžeme jít i o složku výš - do složky, která obsahuje working directory, k tomu používáme zápis: `../`:

- `../main.py` - soubor main.py, který se nachází o složky výše než je working directory, například: soubor v `/home/ja/main.py`, working directory v `/home/ja/skripty/main.py`
- `../../main.py` - soubor main.py, který se nachází o dvě složky výše než je working directory

### Absolutní cesta

Absolutní cesta uvádí cestu k souboru od rootu/kořene adresářového kmene - na Linuxu/Macu tedy začíná rootem neboli `/`, na Windows potom začíná některým z disků `C:/`.
Díky tomu, že absolutní cesta popisuje cestu k souboru kompletně od začátku (rootu) až ke konci (souboru), je zcela nezávislá na working directory.
Pokud chceme umístit konfigurační soubor našeho programu na nějaké místo na disku a vždy jej dohledat, ať už je skript/program nainstalován kdekoliv a je spouštěn odkudkoliv (working directory je kdekoliv), pak je absolutní cesta ideální volba.

Například:
- /home/ja/.config/mujConfig.json
- C:/Users/ja/.config/mujConfig.json

Pozor: vzhledem k odlišnostem, jak jednotlivé operační systémy strukturují jednotlivé důležité složky (například domovskou složku uživatele), je defacto nemožné mít absolutní cestu, která by fungovala na všech operačních systémech.
Jednou z možností je zjistit, na kterém OS je skript spuštěn, a poté pomocí podmínky použít jednu ze 3 cest (každá speciální pro každý OS).

#### Zjištění operačního systému

Pro zjištění operačního systému můžeme použít funkci `platform.platform()` built-in modulu `platform`:

```python
import platform

system = platform.platform()

print(platform)
```

# Práce se soubory

## Otevření souboru

Pro otevření souboru v Pythonu můžeme použít built-in funkci `open()`.
Funkce jako první parametr přijímá cestu k souboru - cesta může být relativní (`nazev.txt`, `slozka/soubor.txt`, `../file.txt`), tak i absolutní (`/home/Honza/soubor.txt` - MacOS, linux; `C:/mydir/myFile.txt` - Windows).
Druhý parametr je volitelný a určuje tzv. mód, v němž je soubor otevřený, defaultní hodnota je: `"rt"`.
Jde o textový řetězec, v němž můžeme kombinovat následující módy otevření souboru:

- `r` - Read - Default value. Opens a file for reading, error if the file does not exist
- `a` - Append - Opens a file for appending, creates the file if it does not exist
- `w` - Write - Opens a file for writing, creates the file if it does not exist
- `x` - Create - Creates the specified file, returns an error if the file exists

a módy toho, jak je soubor interpretován (zda jako textový soubor, nebo zda je otevřen v binární podobě - například videa, obrázky, cokoliv, co defacto není jednoduchý text .txt):

- `t` - Text - Default value. Text mode
- `b` - Binary - Binary mode (e.g. images)

```python
f  = open("mujSoubor.txt", "rt")

#pres radky otevreneho textoveho souboru pote muzeme iterovat
for line in f:
  print(line)

#po tom, co soubor jiz nepotrebujeme je rozumne jej zavrit
f.close()
```

### Automatické zavření souboru - statement WITH .. AS ..

Abychom se nemuseli starat o správné zavření souboru, nabízí Python statement `WITH function AS variable:`.
S jeho pomocí můžeme zavolat funkci a její návratovou hodnotu uložit do proměnné, která bude v následujícím bloku přístupná a po jeho ukončení bude automaticky zavřena/smazána - a to i v případě nečekaného erroru a dalších výjimek.

```python
with open("mujSoubor.txt", "rt") as f:
  for line in f:
    print(line)
  #nemusime volat f.close() o to se postara WITH AS statement

#zde jiz promenna f nebude dostupna, nastane chyba
print(f)
```

## Psaní do souboru

Do textového souboru můžeme zapisovat pomocí metody `write()` objektu souboru.
Pokud jsme zvolili při otevření mód append `a`, pak bude funkce write přidávat řádky na konec souboru, pokud jsme zvolili mód write `w`, pak bude soubor smazán a write bude psát od prvního řádku:

```python
with open("mujSoubor.txt", "w") as f:
  f.write("ahoj svete") #volame metodu write, ktera je dostupna na objektu souboru
  f.write("hello world!")

# a nyni soubor precteme, abychom meli dukaz, ze k necemu doslo
with open("mujSoubor.txt", "r") as f:
  for line in f:
    print(line)

```
