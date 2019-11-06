# Lekce 6

## Kolekce představující mapování

Kolekce představující mapování jsou typy, které podporují operátor příslušnosti `in`, funkci pro zjištění velikosti `len()` a které jsou iterovatelné.
Při iteraci vracejí kolekce představující mapování své prvky v náhodném pořadí.

### Slovníky / Dicitionaries


#### Kopírování seznamů

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


