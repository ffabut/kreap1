# Reference 

Promenne (a obecne vsechny objekty) v Pythonu neobsahuji hodnoty primo, ale obsahuji pouze reference na tyto hodnoty v pameti.
V pripade celych cisel a podobnych jednoduchych datovych typů je to poměrně jednoduché, jelikoz odkazujeme na nemenny objekt, vse je tak relativne intuitivni:

```python
x = 12    # promenna X ukazuje na cislo v pameti obsahujici cislo 12
          # nevytváříme číslo 12, ale pouze říkáme, že X má odkazovat na místo, kde je už předem uložené číslo 12

#         14
#         13
# x ----► 12
#         11
#         10

y = x     # promenna Y ukazuje na stejne misto v pameti jako X, tedy ukazuje na 12
#         14
#         13
# x ----► 12
# y ______▲  11 # posunute jen aby se vesla sipka
#            10 


x = 14    # X nove ukazuje na misto v pameti obsahujici 14, ale Y porad ukazuje na 12
#      __►14
#      |  13
# x ___|  12
# y ______▲  11
#            10

print(x, y) # vse je, jak bychom cekali
```

Když napíšeme `x = 14` tak pouze říkáme: ať proměnná `x` nově ukazuje na 14.
Proměnná `b` ale pořád referuje na původní místo: na číslo 12.
Vše se chová intuitivně a tak, jak bychom čekali.
Co kdyby ale to, na co proměnná odkazuje bylo měnitelné?
Například seznam nebo slovník?
Pak se to začne trochu komplikovat...

## Ověřování referencí

### Funkce id()

Funkce `id()` nám umožňuje zjistit, na jaký objekt proměnná odkazuje, tedy na jakou část paměti proměnná vlastně odkazuje.
Můžeme si tak ověřit, zda dvě proměnné odkazují na stejný objekt, či nikoliv.

```python

seznam1 = [1,2,3]
seznam2 = seznam1
seznam3 = [1,2,3]

print( id(seznam1), id(seznam2), id(seznam3) )
# seznam1 a seznam2 maji stejne ID, jelikoz prirazeni seznam2 = seznam1 priradilo do seznamu2 referenci jaka byla v seznamu1
# seznam3 ma jine ID, jelikoz jsme do nej priradili zcela novy seznam (byt nahodou se stejnymi hodnotami jako v predchozich seznamech)
```

### Operátor IS

Pro zjištění, zda dvě proměnné odkazují na stejné místo v paměti, můžeme použít operátor `is`.
Narozdíl od operátoru `==`, který porovnáva zda jsou hodnoty dvou objektů stejné,
tak operátor `is` porovnává zda identity dvou objektů jsou stejné - tj. jestli odkazují na stejné místo v paměti.

```python
a = 12
b = 12

if a is b:
  print("they refer to the same object")

seznam1 = [1, 2, 3]
seznam2 = seznam1

if seznam1 is seznam2:
  print("they both refer to the same object")
```

## Reference v případě kolekcí

Pokud vytvoříme proměnnou a do ní přiřadíme měnitelnou kolekci, pak skrze proměnnou odkazujeme na měnitelný objekt.
Co to znamená?
Hlavně to, že pokud změníme seznam či slovník, pak bude změněna ve všech proměnných, které na ni odkazují.
Kolekce jsou tedy jen určitým rozcestníkem, informujícím o tom, kde hledat výsledky.
Pokud přiřadíme kolekci do nové proměnné, nezískáme defacto oddělenou kopii, ale pouze odkaz na tu stejnou kolekci.

Je to podobné jako když řekneme doma nebo na bytě a myslíme tím to stejné.
Když uklidíme na bytě, pak bude uklizeno i doma:

```python
doma = ["rozhazene vykresy", "flasky od piva", "elektro bordel"]
# doma odkazuje na seznam ["rozhazene vykresy", "flasky od piva", "elektro bordel"]

byt = doma # byt odkazuje také na seznam ["rozhazene vykresy", "flasky od piva", "elektro bordel"]
# obě proměnné odkazují na stejný objekt - seznam ["rozhazene vykresy", "flasky od piva", "elektro bordel"]

# muzeme si overit, ze obe promenne maji stejne ID -> odkazuji ke stejnemu objektu v pameti
print(id(doma), id(byt))

# narozdíl od jiných typů jsou ale seznamy měnitelné:
doma[0] = "serazene vykresy" # v seznamu, na který odkazuje proměnná original, změníme první prvek
print(doma) # vypíše ["serazene vykresy", "flasky od piva", "elektro bordel"] - přesně tohle jsme čekali!

# ale tohle nás možná překvapí, nebo ne?:
print(byt) # vypíše ["serazene vykresy", "flasky od piva", "elektro bordel"]

byt[1] = "99 Kč"
print(doma, byt)

# Proč? Doma a byt odkazují na stejné místo v paměti
# změnu provádíme v místě, na které proměnná odkazuje, 
# a proto se v obou případech provádí a projevuje na stejném místě 

byt = ["nic", "nic", "nic"] # přestěhování od rodičů na VŠ
# zde neměníme seznam, na který až doposud odkazuje proměnná byt,
# ale namísto toho říkáme, ať byt odkazuje na zcela nové místo v paměti,
# kde je uložen seznam ["nic", "nic", "nic"]

print(byt, doma) # proměnné nyní odkazují na dvě různá místa v paměti
```

Přiřazení tedy nevytváří oddělenou, samostatnou kopii měnitelné kolekce (objektu), ale pouze referenci na stejné místo v paměti - na stejný seznam či slovník jako přiřazovaná proměnná.
Změny na jedné proměnné se tedy projeví i na druhé proměnné, jelikož obě se provedou na stejné kolekci, na níž obě proměnné odkazují.

Pokud bychom chtěli vytvořit samostatnou kopii kolekce, musíme importovat modul `copy` a použít jeho funkce `copy.copy()` či `copy.deepcopy()`.

## Mělká kopie (shallow copy) - copy.copy()

Chceme-li vytvořit skutečnou kopii kolekce, máme dvě možnosti: mělké nebo hluboké kopie.
Začneme u mělké kopie.
Jako první musíme importovat modul `copy` a z něj volat funkci `copy()`.
Funkce `copy()` vrací oddělenou samostatnou kopii kolekce, jakékoliv úpravy na této kolekci se tak nepromítnou na původní kolekci, či naopak.

```python
import copy

doma = ["rozhazene vykresy", "flasky od piva", "elektro bordel"]

byt = copy.copy(doma) #funkce copy vrati oddelenou kopii kolekce

print(doma, byt) #obe kolekce sice obsahuji totozne hodnoty

# ale odkazuji k dvema rozdilnym objektum, maji rozdilne ID:
print(id(doma), id(byt))

doma[0] = "serazene vykresy" #obe promenne odkazuji na dve ruzne kolekce, tedy pri zmene prvku v kolekci se zmena nepromitne i na druhe kolekci
byt[2] = "serazene soucastky"

print(doma, byt)
```

Pozor: funkce `copy()` se sice postará o zkopírování kolekce, ale již se nepostará o všechny další pod-kolekce, které může tato kolekce obsahovat.
Kolekce v kolekci tak mohou dále sdílet reference a být "propojené":

```python
import copy

pravda = [True, True, True]
laska = ["<3", "<3"]

havel1 = [pravda, laska]
havel2 = copy.copy(havel1)

havel2[1] = "LÁSKA!"
print(havel1, havel2) # havel2 odkazuje na oddeleny objekt, na nem jsme zmenili druhy prvek - odkaz na seznam jsme zmenili na textovy retezec, zmena se v havel1 neprojevila

#ale pozor:
havel2[0][2] = False # havel2 odkazuje na oddeleny objekt, jeho prvnim clenem je seznam, ktery odkazuje nekam do pameti,
# na stejne misto odkazuje i havel1, byt havel1 a havel2 jsou dva oddelene seznamy:

print(havel1, havel2)

#vyjasnist nam to muze funkce id()
print( id(havel1), id(havel2)) # dve ruzne ID, protoze jsme pouzili funkci copy()
# ale POZOR: jednotlive podkolekce muzou mit porad stejne ID:
print( id(havel1[0]), id(havel2[0]))

# neboli:
print( havel1[0] is havel2[0] ) #= TRUE
```

## Hluboká kopie (deep copy) - copy.deepcopy()

Abychom se vyhnuli tomu, že zkopírovaná kolekce bude stále obsahovat pod-kolekce, které budou mít stejné ID a tedy budou odkazovat na jedno místo v paměti, pak můžeme použít funkci `deepcopy()`.
Ta zajistí, že nejenže kopírovaná kolekce, ale ani žádné další kolekce v ní obsažené nebudou sdílet reference - `deepcopy()` vytvoří oddělené kopie všech obsažených kolekcí:

```python
import copy

pravda = [True, True, True]
laska = ["<3", "<3"]

havel1 = [pravda, laska]
havel2 = copy.deepcopy(havel1)

print( id(havel1), id(havel2)) # obe hlavni kolekce maji rozdilne ID
print( id(havel1[0]), id(havel2[0])) # rozdilne ID maji ale i jednotlive pod-kolekce!

havel2[0][2] = False # tato zmena se tedy jiz neprojevi v promenne havel1

print(havel1, havel2)
```
