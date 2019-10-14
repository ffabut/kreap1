# Funkce a Metody

Funkce nám umožňují zabalit určitou část kódu a pak ji moct volat/spouštět z různých míst v programu.
Také nám umožňují tento kód parametrizovat - spouštět s různými počátečními hodnotami a tak mírně měnit jeho průběh, to co dělá.

Každá funkce:
- má své jméno,
- může očekávat a být volána s žádným, jedním či více parametry - oddělujeme je čárkou,
- může mít návratovou hodnotu - výsledek,
- pokud funkce nevrací hodnotu, pak python i tak vrátí hodnotu `None`.

Nejjednodušší je volání funkce bez parametru a bez uložení návratové hodnoty, vypadá to takto:

```python
# voláme funkci, která se jmenuje print()
print() # prázdné závorky jsou nutnost
```

Předešlá funkce, jak již víme, vypíše prázdný řádek.
Zkusíme tedy přidat parametr, toto jsme již také dělali:

```python
# voláme funkci print s jedním parametrem
print("Hello World!") # parametrem je textový řetězec "Hello World!"

# jako parametr ale můžeme použít také proměnou
pozdrav = "Čau světe!"
# voláme funkci print s jedním parametrem
print(pozdrav) # parametrem je proměnná pozdrav, která odkazuje k hodnotě "Čau světe!"
```

Funkce print má za úkol tisknout do příkazové řádky, má něco vykonávat, nikoli počítat.
Print tak nemá návratovou hodnotu, nebo přesněji: její návratovou hodnotou je `None`.

```python
navratovaHodnota = print("Hello world")
print(navratovaHodnota)
```

Příkladem funkce, která spíš nic nedělá a místo toho jde o její výsledek, tedy o její návratovou hodnotu, je například built-in funkce `pow()`:

```python
# funkce pow() mocni cislo na x-tou, prvním parametrem je mocněnec, druhým parametrem je mocnitel:
# pow(mocnenec, mocnitel)

# volame funkci pow() se dvema parametry - 2 a 4
navratovaHodnota = pow(2, 4) # pow(2,4) má význam stejný jako 2**4, tedy dva na čtvrtou = 16

# muzeme si predstavit, ze vysledkem, navratovou hodnotou, python za behu programu nahradi volani funkce
# vlastne se tedy stane:
# navratovaHodnota = pow(2, 4)
# navratovaHodnota = 16

# navratova hodnota neni None, ale je integer - výsledek po mocnění
print(navratovaHodnota)
```

Některé funkce vyžadují přesný počet a přesný typ parametrů, jinak dojde k chybě.
Jiné funkce zvládnout specifické počty parametrů, například `pow()` v konečném důsledku umí:

```python
pow(5)       # == 25, ekvivalent 5**2
pow(5, 3)    # == 125, ekvivalent 5**3
pow(5, 3, 2) # == 1, ekvivalent 5**3 % 2, ale rychlější, je trochu divné/nečekané, že toto funkce pow() umí, ale umí to
```

Některé funkce zvládnout téměř neomezené počty parametrů, případně zvládnou nejrůznější datové typy.
Příkladem budiž print():

```python
print(None, True, "dva", 3, 4.0)
```

## Built-in funkce

Python obsahuje předdefinované, built-in funkce, které můžeme rovnou použít.
Některé z nich již známe:
- print() - tiskne do příkazové řádky
- input() - čeká na vstup uživatele z příkazové řádky, může mít parametr, který uvede vstup: `input("zadejte jméno:")`
- int() - převede float, případně string obsahující pouze číslo, na integer
- float() - převede integer, případně string obsahující pouze číslo, na float
- str() - převede integer nebo float na string
- bool() - převede integer, float, string na bool(), False = 0, 0.0, "", všechno ostatní je True
- abs() - absolutní hodnota
- pow() - mocnina
- round() - zaokrouhlení

Python obsahuje i velké množství dalších užitečných built-in funkcí, ke kterým se dostaneme později - souvisejí s pozdějšími tématy.

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

