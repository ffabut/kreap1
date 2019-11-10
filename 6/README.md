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

---

Poznámka: pokud bychom rádi neexistující klíč i s hodnotou rádi rovnou vložili do slovníku, pak můžeme použít metodu setdefault():

```python
slovnik = {"klic" : "hodnota", "key" : 12, "dog": "pes"}
neexistujici = slovnik.setdefault("art", "cool") # art neni klic ve slovniku, proto metoda vlozi novou dvojici "art":"cool"
# a vrati hodnotu "cool" - pokud bychom zakladni hodnotu nezadali, pak by se pouzilo None
print(neexistujici) # vypise: "cool"
print(slovnik) #vypise: {"klic" : "hodnota", "key" : 12, "dog": "pes", "art" : "cool"}
```

---

TODO:....

### Kopírování seznamů

Jak jsme si rekli v predeslych hodinach: promenne v Pythonu neobsahuji hodnoty primo, ale obsahuji pouze odkazy na tyto hodnoty v pameti.
V pripade cely cisel a podobnych jednoduchych promennych to nedela problem, jelikoz nebudeme menit hodnotu ulozenou pod adresou v pameti odpovidajici cislu 7 - adresa cisla 7 a hodnota tam ulozena (7) tak budou porad stejne. V pripade seznamů ale tyto hodnoty můžeme měnit a to vyvolává pár problému.

##### Přiřazení není kopie, ale odkaz na stejný seznam

```python
seznam = [1, 2, 3]
druhy = seznam # do promenne druhy neukladame kopii seznamu seznam, ale odkaz na tento seznam

# obe promenne seznam i druhy odkazuji ke stejnemu mistu v pameti
# pokud zmenime jedno, zmeni se i to druhe:

seznam[0] = "jedna"
druhy[2] = "tri"
print(seznam)
print(druhy)
```

Toto je trochu zakerne a necekane chovani, je treba na nej pamatovat.

##### Mělká kopie

Seznamy můžeme skutečně kopírovat pomocí 


