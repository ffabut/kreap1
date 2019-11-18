# Odkazy 

### Kopírování kolekcí

#### Úvod - obecně o objektech

Jak jsme si rekli v predeslych hodinach: promenne (a obecne vsechny objekty) v Pythonu neobsahuji hodnoty primo, ale obsahuji pouze odkazy na tyto hodnoty v pameti.
V pripade celych cisel a podobnych jednoduchych promennych to nedela problem, jelikoz odkazujeme na nemenny objekt, vse je tak relativne intuitivni:

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

Když napíšeme `x = 12` tak pouze říkáme: ať X ukazuje na 12.
Prakticky to pak znamená, že X je 12.

#### Odkazy v případě kolekcí

Pokud ale vytvoříme proměnnou a do ní přiřadíme slovník, pak skrze proměnnou odkazujeme na měnitelný objekt.
Co to znamená?
Například to, že pokud změníme kolekci, pak bude změněna ve všech proměnných, které na ni odkazují.
Je to podobné jako když řekneme doma nebo na bytě a myslíme tím to stejné.
Když uklidíme na bytě, pak bude uklizeno i doma:

```python
doma = ["rozhazene vykresy", "flasky od piva", "elektro bordel"]
# doma odkazuje na seznam ["rozhazene vykresy", "flasky od piva", "elektro bordel"]

byt = doma # byt odkazuje také na seznam ["rozhazene vykresy", "flasky od piva", "elektro bordel"]
# obě proměnné odkazují na stejný objekt - seznam ["rozhazene vykresy", "flasky od piva", "elektro bordel"]

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

Přiřazení tedy nevytváří kopii kolekce(obejktu), ale pouze proměnnou, která odkazuje na stejné místo jako přiřazovaná proměnná.

#### Mělká kopie

Chceme-li vytvořit skutečnou kopii kolekce, máme dvě možnosti: mělké nebo hluboké kopie.
Začneme u mělké kopie: 






Stejně jako běžné proměnné a všechny objekty v Pythonu i kolekce neuchovávají hodnoty přímo, ale pouze na ně pouze odkazují.
Kolekce jsou tedy jen určitým rozcestníkem, informujícím o tom, kde hledat výsledky.
Pokud přiřadíme kolekci do nové proměnné, nezískáme defacto oddělenou kopii, ale pouze odkaz na tu stejnou kolekci:
