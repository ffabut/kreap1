# Lekce 6

## Kolekce představující mapování

Kolekce představující mapování jsou typy, které podporují operátor příslušnosti `in`, funkci pro zjištění velikosti `len()` a které jsou iterovatelné.
Při iteraci vracejí kolekce představující mapování své prvky v náhodném pořadí.

### Slovníky / Dicitionaries

Slovníky, tedy typ `dict`, představují neuspořádanou měnitelnou kolekci nula či více dvojic klíč a hodnota.
Klíče jsou libovolné hashovatelné hodnoty - především řetězce, čísla atd..., skrze které můžeme přistupovat k nim přiřazeným hodnotám různých typů.
Stejný klíč se nemůže vyskytovat dvakrát - je vždy unikátní.
Slovník definujeme ve složených závorkách, přičemž dvojice klíčů a hodnot oddělujeme čárkami a mezi klíčem a hodnotou vkládáme dvojtečku, tedy například takto:

```python
# definice slovniku
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes", 1989 : "revoluce"}

# ziskani hodnoty ze slovniku
print(slovnik["klic"]) # vypise: hodnota
print(slovnik["key"]) # vypise: 12
print(slovnik[1989]) # vypise: revoluce

# vypsani celeho slovniku
print(slovnik) # vypise: {"klic" : "hodnota", "key" : 12, "dog": "pes", 1989 : "revoluce"}
```

Pozor: nemůžeme přistupovat ke klíčům ve slovníku skrze hodnoty, jaksi obráceně.
Důvodem je určitě to, že v jednom slovníku můžeme mít více stejných hodnot pod různými klíči a pak by nebylo jasné, jaký klíč chceme.
Příklad:

```python
slovnik = {"dog" : "pes", "hound" : "pes"}

print(slovnik["dog"]) #vypise: pes
print(slovnik["hound"]) #vypise: pes

# toto ale nejde:
print(slovnik["pes"]) #klic neni ve slovniku, nastane chyba
# kdyby nenastala, co by se melo vypsat? dog nebo hound? Proto nemuzeme pristupovat ke klicum pres hodnoty
```

#### Změna hodnoty a vkládání zcela nové dvojice klíč-hodnota

Chceme-li změnit hodnotu uloženou pod klíčem, pak jednoduše přiřadíme k tomuto klíču novou hodnotu:

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}
slovnik["key"] = 66 #pod klici "key" priradime novou hodnotu 66

print(slovnik) #vypise: {"klic" : "hodnota", "key" : 66, "dog": "pes"}
```

Pokud vložíme hodnotu pod klíč, který neexistuje, vytvoříme tím novou dvojici hodnota-klíč:

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}
slovnik["car"] = "auto" #ve slovniku je nyni nova dvojice car:auto

print(slovnik) # vypise: {"klic" : "hodnota", "key" : 12, "dog": "pes", "car" : "auto"}
```

---
Úkol1: Napište program, který bude počítat účasti na hodinách: uživatelka zadá jméno člověka (klíč) a program mu zvětší počet účastí (hodnotu) o 1.
Bude se vám hodit slovník se jmény studentů, nekonečný cyklus while a funkce input().
Řešení [zde](ukol1.py).

#### Smazání dvojice klíč-hodnota

Ke smazání hodnoty ze slovníku se používá klíčové slovo `del`:

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}
del slovnik["klic"]

print(slovnik) # vypise: {"key" : 12, "dog": "pes"}
```

#### Procházení/iterace přes dvojice ve slovníku

Přes klíče slovníků je možné procházet pomocí cykly `for` - jelikož jsou slovníky neuspořádané, tak jsou klíče vraceny v náhodném pořadí.
Pomocí klíče pak můžeme přistupovat k jednotlivým hodnotám:

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}

for key in slovnik:
    print(key) # vypise klic, napriklad: klic, key, dog
    print(slovnik[key]) #skrze klic pristupujeme k hodnote, vypise hodnoty, napriklad: hodnota, 12, pes

    #slovnik pak muzeme klidne menit:
    slovnik[key] = "nic"

print(slovnik) # vypise: {"klic" : "nic", "key" : "nic", "dog": "nic"}
```

---
Úkol2: Napište program na procvičování slovíček.
Program napíše uživatelce české slovo a bude se ptát na jeho anglickou verzi - v případě neuhodnutí napíše řešení a pak se půjde na další slovíčko.
Bude se vám hodit slovník, input() a cyklus for.
Řešení [zde](ukol2.py).

#### Zjištění příslušnosti: operátor `in`

Zjištění existence klíče ve slovníku je možné za použití operátoru `in`:

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}

if "dog" in slovnik:
    print("dog je klicem slovniku")
else:
    print("dog neni klicem ve slovniku")
```

Operátor `in` se hodí, pokud chceme přistupovat k hodnotě uložené pod klíčem, ale nevíme, zdali je klíč ve slovníku nebo nikoli.

---
Úkol3: Napište deluxe verzi programu počítacího absenci.
Program bude počítat účasti na hodinách: uživatelka zadá jméno člověka (klíč) a program mu zvětší počet účastí (hodnotu) o 1.
Nově program přijímá i nová jména, zkrátka kohokoliv on the fly.
Slovník je v počátku zcela prázdný.
Bude se vám hodit prázdný slovník, nekonečný cyklus while, operátor `in` a funkce input().
Řešení [zde](ukol3.py).

#### Metoda get()

Metoda slovníku `get()` nám umožňuje přistoupit k hodnotě uložené pod klíčem - a pokud klíč neexistuje, pak nedostat chybu, ale námi udanou defaultní hodnotu, případně `None` pokud defaultní hodnotu neuvedeme:
Například:

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}

existujici = slovnik.get("key", 110) #klic key existuje, takze metoda vrati hodnotu pod timto klicem, tedy 12 - nami udana defaultni hodnota je ignorovana
# neexistujici = slovnik["yes"] # zde by doslo k chybe, ale pres metody get bude vse ok:
neexistujici = slovnik.get("yes", 110) #klic yes neexistuje, metoda vrati nami zadanou defaultni hodnotu 110
jedenParametr = slovnik.get("anthopocene") # klic anthropocene neexistuje, nezadali jsme defaultni hodnotu, metoda proto vrati None

print(existujici, neexistujici, jedenParametr) # vypise: 12, 110, None
```

#### Metoda setdefault()

Pokud chceme, stejně jako v případě metody `get()`, získat hodnotu a v případě neexistujícího klíče užít defaultní hodnotu, můžeme použít také metodu `setdefault()`.
Narozdíl od `get()` však metoda `setdefault()` případně rovnou i vloží neexistující dvojici klíč:defaultní-hodnota do slovníku.
Pro příště tak už bude klíč a hodnota rovnou dostupná ve slovníku:

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}
neexistujici = slovnik.setdefault("art", "cool") # art neni klic ve slovniku, proto metoda vlozi novou dvojici "art":"cool"
# a vrati hodnotu "cool" - pokud bychom zakladni hodnotu nezadali, pak by se pouzilo None
print(neexistujici) # vypise: "cool"
print(slovnik) #vypise: {"klic" : "hodnota", "key" : 12, "dog": "pes", "art" : "cool"}
```

#### Metoda pop()

Pomocí metody `pop()` můžeme přistoupit ke hodnotě pod klíčem a poté dvojici klíč-hodnota odstranit ze slovníku:

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}

print(slovnik.pop("dog")) # vypise: pes a odstrani dvojici ze slovniku
print(slovnik) # dog:pes jiz neni ve slovniku, vypise: {"klic" : "hodnota", "key" : 12}

# pokud klic neni ve slovniku, nastane chyba keyError
# tomu muzeme predejit tim, ze uvedeme defaultni hodnotu

print(slovnik.pop("cat", "kocka")) # vypise: kocka, a dale nic, dvojice neni ve slovniku a tak ji netreba odstranovat
print(slovnik) # cat:kocka nebyla a neni ve slovniku, vypise: {"klic" : "hodnota", "key" : 12}
```

## Další užitečné funkce a operace s kolekcemi

### Sčítání posloupností

Posloupnosti můžeme sčítat pomocí operátoru `+`.
Druhá posloupnost bude navázána za tu první:

```python
s = (1, 2, 3)
t = (30, 31, 32)

x = s + t # secte dve posloupnosti, druha 
print(x) # vypise: (1, 2, 3, 30, 31, 32)
```

### Násobení posloupností

Násobení dává smysl pouze u posloupností, u neseřazených kolekcí jako množiny a slovníky nedává smysl.
Posloupnosti můžeme násobit celým číslem, užití je následující:

```python
den = ["dopoledne", "odpoledne", "brzká noc", "pozdní noc"]
tyden = den * 7

print(tyden) # vypise: ["dopoledne", "odpoledne", "brzká noc", "pozdní noc", "dopoledne", "odpoledne", "brzká noc", "pozdní noc", "dopoledne", ...... , "pozdní noc"]
```

### Funkce len() pro zjištění velikosti kolekce

Pokud chceme zjistit, jak velká je kolekce, kolik má prvků, pak můžeme použít built-in funkci `len()`:

```python
ntice = (1, 2, 3)
seznam = [1, 2]
mnozina = {1, 2, 3, 4, 4, 5} # pozor prvek 4 je duplicitni, coz v mnozine nejde, vysledek je tedy defacto {1, 2, 3, 4, 5}
slovnik = {"jedna": 1, 2: "dva"}

print("velikost ntice:", len(ntice))      # 3
print("velikost seznamu:", len(seznam))   # 2
print("velikost mnoziny:", len(mnozina))  # 5
print("velikost ntice:", len(slovnik))    # 2
```
### Otočení směru iterace přes posloupnost

Občas se může hodit procházet přes posloupnosti v opačném směru, tj. od konce k začátku, k tomu můžeme použít built-in funkci `reversed()`.
Ale pozor: tato funkce nevytváří obrácenou kopii posloupnosti, pouze iterátor, který bude procházet posloupností naopak.
Hodí se tak používat hlavně v kombinaci s `for` cyklem.
Ale ne k vytváření otočené posloupnosti a jejího uložení do proměnné:

```python
ntice = (1, 2, 3, 4, 5)

for x in reversed(ntice):
    print(x)

x = reversed(ntice)
print(x) #vytiskne: <reversed object at 0x7f1c6d11c6d0> neboli adresu iteratoru
# neda se s tim pracovat jako s beznou posloupnosti
```

### Převod kolekcí na jiný typ kolekce

Kolekce můžeme převádět na kýžený typ kolekce pomocí funkcí `tup()`, `list()`, `set()`:
```python
ntice = (1, 2, 3, 4, 5, 4)
seznam = ["a", "b", "c"]
mnozina = {90, 91, 92}
slovnik = {"x": "XX", "y": "YY"}

# prevod na tuple s funkci tuple():
print(tuple(ntice))     # (1, 2, 3, 4, 5, 4) 
print(tuple(seznam))    # ("a", "b", "c")
print(tuple(mnozina))   # (90, 91, 92)   - poradi muze byt i jine
print(tuple(slovnik))   # ("x", "y")

# prevod na seznam s funkci list():
print(list(ntice))     # [1, 2, 3, 4, 5, 4] 
print(list(seznam))    # ["a", "b", "c"]
print(list(mnozina))   # [90, 91, 92]   - poradi muze byt i jine
print(list(slovnik))   # ["x", "y"]

# prevod na mnozinu s funkci set()
# mnozina nemuze obsahovat vice stejnych prvku, proto duplicitni prvky nebudou soucasti vysledku:
print(set(ntice))     # {1, 2, 3, 4, 5} - prvek 4 byl duplicitni, v mnozine muze byt pouze jednou
print(set(seznam))    # {"a", "b", "c"}
print(set(mnozina))   # {90, 91, 92}   - poradi muze byt i jine
print(set(slovnik))   # {"x", "y"}
```

### Kopírování kolekcí

Na tuto trochu složitější problematiku se podíváme v další lekci.

## Procvičování

Úkol4: Naplánujte program, který bude překládat/zaměňovat určitá slova v textu.
Jak bychom tento program postavili?
Zkuste si naplánovat architekturu programu.
Co bude potřeba udělat s textem a podobně...
Možné řešení [zde](ukol4.py).

Úkol5: Zkuste program z úkolu 4 zrealizovat.
Bude se vám hodit proměnná obsahující vstupní text, slovník obsahující dvojice slov, metoda řetězců `split()` a for loop.
Řešení [zde](ukol5.py).
