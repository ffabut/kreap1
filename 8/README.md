# Lekce 8

V této lekci se podíváme na třídy a metody.
Ty jsme již používali v předchozích lekcích, aniž bychom o tom věděli.
Nyní si je proto zkusíme trochu víc přiblížit.

## Třídy (Class)

Třídy jsou způsobem, jak v Pythonu vytvořit entity, které mohou držet jak vlastní data v proměnných, tak vlastní sady funkcí - metod.
Jednoduše tak můžeme vytvořit vlastní datové typy, které můžou přesně odpovídat podobě dat, s nimiž chceme pracovat.

Příklad:
```python
class uzivatelka: #zde definujeme tridu uzivatelka, je to urcity popis objektu, recept
    vek = 30
    email = "mail@gmail.com"

eva = uzivatelka() #zde vytvarime z tridy uzivatelka jednu jeji novou instanci a ulozime ji do promenne eva, zavorky jsou nutne

print(eva.vek) #k promennym v instanci muzeme pristupovat pomoci tecky
eva.email = "eva@seznam.cz"
print(eva.email)
```

### Vytváření tříd

Třídy definujeme pomocí klíčového slova `class`, za nímž následuje název třídy, dvojtečka a v bloku poté již popisujeme samotnou třídu.
V třídě můžeme vytvářet jak nové proměnné (v tridach se nazyvaji atributy), tak funkce (když jsou v třídách, tak jim říkáme metody).
Jediným rozdílem v případě metod je to, že jako první parametr musí mít klíčové slovo `self`, které označuje třídu samotnou - přes self můžeme přistupovat k proměnným a dalším funkcím třídy.
Lepší ale bude to rovnou ukázat:

```python
class uzivatelka: # definice tridy
    vek = 30 # vytvarime promennou vek ve tride
    email = "mail@gmail.com"

    def setMail(self, newMail): # definujeme metodu setMail, argument self je povinny 
        self.email = newMail # k promennym (a dalsim metodam) v ramci tridy
        # pristupujeme skrze klicove slovo self oznacujici celou tridu

jan = uzivatelka() # jedna instance tridy uzivatelka
eva = uzivatelka() # druha instance tridy uzivatelka

eva.setMail("evaeva@gmail.com") # volame metodu setMail, kterou jsme definovali v tride uzivatelka
#argument self nemusime uvadet, odkaz na objekt prida jako prvni parametr python automaticky

print(eva.email) # vypise upraveny email
print(jan.email) # vypise puvodni email, objekt/instanci "jan" jsme nijak nemenili

# jak je videt, kazda instance si drzi oddelene kopie promennych - jsou na sobe zcela nezavisle
```

### Metoda __init__

Když vytváříme instanci z třídy (`eva = uzivatelka()`), tak voláme název třídy se závorkami.
Celé to vypadá, jako bychom spíše volali funkci - a taky to tak je: voláme iniciační funkci třídy.
V jejím rámci Python připraví místo v paměti na novou instanci třídy a do ní poté tuto instanci uloží.

Vše probíhá automaticky a nemusíme se o nic starat.
Občas se ale hodí při tomto procesu udělat také nějakou naši práci - například generovat heslo, cokoliv...
K tomu můžeme použít metodu `__init__` (dvě podtržítka init dvě podtržítka), tato metoda bude spuštěna Pythonem pokaždé, když se vytváří nová instance třídy:

```python
class uzivatelka: # definice tridy
    vek = 30 # vytvarime promennou vek ve tride
    email = "mail@gmail.com"

    def __init__(self): #metoda init bude nove informovat o vytvoreni nove instance...
        print("prave je vytvarena nova instance tridy uzivatelka...")

    def setMail(self, newMail): # definujeme metodu setMail, argument self je povinny 
        self.email = newMail # k promennym (a dalsim metodam) v ramci tridy
        # pristupujeme skrze klicove slovo self oznacujici celou tridu


martin = uzivatelka() #vytvarime novou instanci tridy uzivatelka
# behem toho se spusti metoda init, ktera vypise info... "prave je vytvarena nova instance tridy uzivatelka..."
```

Metodu `__init__` muzeme take rozsirit o dalsi argumenty.
Dosahneme tak toho, ze nase trida pujde iniciovat pouze s danymi parametry - napriklad pokud chceme, aby uzivatelka mela jasne zadany vek a email:

```python
class uzivatelka: # definice tridy
    def __init__(self, vek, email): #init nyni vyzaduje argument vek a email
        self.vek = vek # promenne muzeme vytvaret take pres self.jmenoPromenne
        self.email = email

    def printInfo(self): 
        print("vek:", self.vek)
        print("email:", self.email)

# martin = uzivatelka() # toto by uz neslo, metoda uzivatelka nyni vyzaduje 2 argumenty pro sve vytvoreni

martin = uzivatelka(27, "martin@gmail.com")
martin.printInfo()
```

Poznámka: proměnné užívané v třídě je ideální definovat právě v metodě `__init__` a nikoliv přímo v třídě.
Pokud bychom definovali proměnné přímo v třídě, mohlo by se za určitých okolností stát, že by nebyly unikátní pro každou instanci třídy, ale byly by sdílené pro všechny instance jedné třídy.
To by se mohlo stát například, pokud bychom definovali seznam přímo v třídě.
Obecně je proto lepší definovat proměnné v metodě init, případně v jiných metodách, nikoliv přímo v třídě.

Úkol1: vytvořte třídu `klauzura`, která bude obsahovat data potřebná při obhajobě díla u klauzur.
Například: jméno autorky, rok, název, médium, hodnocení atd...
Metoda init by mohla hezky vybízet k zadání potřebných dat.
A kromě toho by třída měla obsahovat metodu `hodnotit`, která umožní zadat známku od komise.
Řešení [zde](ukol1.py).

### Dědičnost tříd

Třídy podporují dědičnost - tedy schopnost vytvořit třídu, která bude mít za vzor nějakou již existující třídu.
Tato nová třída bude mít všechny atributy a metody původní třídy, ale navíc do ní můžeme dodat nové atributy a metody, tedy ji rozvinout, specializovat.
To je praktické v situaci, kdy víme, že objekty, s kterými chceme pracovat, mají nějaký společný základ, ale dále se již trochu liší.
Díky dědičnosti můžeme udělat jednu obecnou třídu, která bude předlohou pro několik dalších, specializovaných.

Pokud chceme, aby třída dědila z jiné třídy, uvedeme rodičovskou třídu do závorek po názvu námi definované třídy:

```python
class human:
    def __init__(self, vek, jmeno):
        self.vek = vek
        self.jmeno = jmeno

    def talk(self):
        print("blablabla...")

class singer(human):
    def sing(self):
        print("lalalalalalaaaaa!")

honza = human(55, "Honza")
karel = singer(33, "Karel")

honza.talk()
karel.talk() # metoda talk byla v tride singer podedena od tridy human

karel.sing()
honza.sing() # zde nastane chyba, objekt honza je trida human, ta ale nema metodu sing()
```







funkce super() k pristupovani k metodam rodice...

