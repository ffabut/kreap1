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

#### Class Expansion/Subclassing
Výše zmíněný kód je příkladem tzv. expandování neboli subclassingu.
Jde o koncepční přístup, kdy vytváříme novou třídu na základě již existující třídy a pouze ji rozšiřujeme o nové metody a atributy.
Třída `singer` je tedy rozšířením třídy `human` o metodu `sing`, v chování `__init__` a `talk` se nic nemění.
Fakticky nepřepisujeme nic z původní třídy, pouze ji rozšiřujeme.

Výhodou expandování/subclassingu je jednoduchost a přehlednost kódu, pro začátek je to docela dobrý a lehce pochopitelný přístup.
Občas nám to ale nemusí stačit a budeme potřebovat modifikovat i chování metod a atributů původní třídy, od čehož můžeme použít tzv. modifikaci neboli overriding.

#### Class Overriding
Při overridingu přepisujeme některé metody a atributy původní třídy (a samozřejmě také můžeme přidat nové jako v případě expandování).
Overriding nám umožňuje přizpůsobit chování třídy, která dědí, našim potřebám, aniž bychom museli vytvářet zcela novou třídu, nebo vytvářet alternativní metody a ty zděděné nepoužívat.

```python
class human:
    def __init__(self, vek, jmeno):
        self.vek = vek
        self.jmeno = jmeno

    def talk(self):
        print("blablabla...")

class singer(human):
    def sing(self): # EXPANDOVANI
        print("lalalalalalaaaaa!")

    def talk(self): # OVERRIDING
        print("blábláblá... (zpěvně)")

honza = human(55, "Honza")
karel = singer(33, "Karel")

honza.talk() # bude použita human.talk(), protože honze je instance tridy human
karel.talk() # bude použita singer.talk(), protože karel je instance tridy singer a v ni je prepsana metoda talk()

karel.sing() # probehne diky expandovani
honza.sing() # zde nastane chyba, objekt honza je trida human, ta ale nema metodu sing()
```

Overriding je možný díky tomu, že Python nejprve hledá metodu v třídě, ve které je objekt vytvořen, a pokud ji nenajde, hledá ji v rodičovské třídě.
Ověřit si pořadí můžeme pomocí metody `mro()` (Method Resolution Order), která nám vrátí pořadí, v jakém Python hledá metody v třídě.
Více v části MRO.

#### Indirection neboli přistupování k metodám rodiče - super()
Overriding může být užitečný, ale může také způsobit problémy, pokud chceme v metodě potomka použít kód již implementovaný v metodě rodiče.
Overridem se vlastně připravíme o vše, co bylo v metodě rodiče.
Abychom se tomu vyhnuli, můžeme použít funkci `super()`, která nám umožní přistupovat k metodám rodiče.

Pokud voláme funkci `super()` bez parametrů, získáme objekt představující rodičovskou třídu, a na něm pak můžeme volat metody tohoto rodiče, které chceme použít.

```python
class human:
    def __init__(self, vek, jmeno):
        self.vek = vek
        self.jmeno = jmeno

    def talk(self):
        print("blablabla...")

class singer(human):
    def sing(self): # EXPANDOVANI
        print("lalalalalalaaaaa!")

    def talk(self): # OVERRIDING s pouzitim super()
        super().talk() # zavolame metodu talk z rodicovske tridy, v pseudo kodu: human.talk()
        print("...a teď si zazpívám") # a tady si doimplementujeme, co chceme

honza = human(55, "Honza")
karel = singer(33, "Karel")

honza.talk() # bude použita human.talk(), protože honze je instance tridy human
karel.talk() # bude použita singer.talk(), protože karel je instance tridy singer a v ni je prepsana metoda talk()

karel.sing() # probehne diky expandovani
honza.sing() # zde nastane chyba, objekt honza je trida human, ta ale nema metodu sing()
```

Poznámka: super() ve své podstatě jen vrací proxy objekt další třídy v MRO (Method Resolution Order), toto je zejména podstatné, když dědíme z více tříd.

### MRO - Method Resolution Order
MRO je algoritmus, který Python používá k určení pořadí, v jakém hledá metody v třídě.
MRO je důležitý zejména v případě, kdy třída dědí od více tříd, nebo kdy se v třídě vyskytuje dědičnost.
Pokud chceme zjistit přesné pořadí, v jakém Python hledá metody u dané třídy, můžeme použít parameter třídy `__mro__` nebo metodu `mro()`:

```python
singer.__mro__
singer.mro()
>>> (<class 'singer'>, <class 'human'>) 
```


Případně, pokud nechceme získat MRO pro konkrétní třídu, ale pro instanci, můžeme použít `__class__` k získání třídy dané instance a na ní pak zavolat `__mro__`/`mro()`:

```python
karel.__class__.__mro__
karel.__class__.mro()
>>> (<class 'singer'>, <class 'human'>) 
```

Tedy Python se prvně podívá do singer, pokud tam nenajde metodu, podívá se do human.

MRO se hodí zejména v případě, kdy máme složitější dědičnost, kdy třída dědí od více tříd, nebo kdy se vyskytuje dědičnost v dědičnosti.

### Dědičnost z více tříd
Python umožňuje dědit i z více tříd, což může být užitečné, pokud chceme kombinovat vlastnosti více tříd.

```python
class Base:
    def __init__(self):
        print("Base init")

class A(Base):
    def __init__(self):
        print("A init")
        super().__init__()

class B(Base):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()

# Create an instance of C
c = C()
```

Výstup bude:
```
C init
A init
B init
Base init
```

Proč tento výstup a nikoliv `C init, A init, Base init`?
Jak se zavolalo `B init`?
Super() používá MRO k určení pořadí, v jakém se získávají rodičovské třídy.
1. Když C volá `super().__init__()`, Python se podívá na MRO třídy C, která je `C -> A -> B -> Base` a tedy zaolá `A init`.
2. V `A init` je opět voláno `super().__init__()`, Python se podívá na MRO (ale našeho C), další v pořadí je B, tedy v tomto případě A vlastně nebude volat Base, ale skrze super dostane B.
3. V `B init` je opět voláno `super().__init__()`, Python se podívá na MRO (ale našeho C), další v pořadí je Base, které by bylo tak jako tak.
4. V `Base init` se vytiskne `Base init`.

## Kde se prakticky setkáváme s třídami?
Praktický příklad použití tříd je například to, jak Python zachází s výjimkami nebo Exception.
Výjimky jsou v Pythonu reprezentovány třídami, které dědí od třídy `BaseException`.
Můžeme se ale setkat s [řadou dalších Exceptions](https://docs.python.org/3/library/exceptions.html), například: `ValueError`, `TypeError`, `ZeroDivisionError` atd.
A dokonce můžeme vytvářet vlastní výjimky, které dědí od `BaseException` nebo některé z dalších více specializovaných výjimek, což může být praktické, pokud chceme někde raisovat výjimku, která bude mít specifické chování, název, atd.

Proč nemít jen BaseException a všechny výjimky řešit pomocí ní?
Mít více výjimek umožňuje nám lépe rozlišit, co se stalo, a tím i lépe reagovat.
Například skrze try-except blok můžeme zachytit specifickou výjimku a podle toho, co se stalo, reagovat jinak:

```python
import random
try:
    x = 10 / random.randint(0, 1) # zde muze byt deleni nulou
    a = random.choice([1, 2.5, "3"])
    vysledek = a + x # zde muze byt chyba TypeError, protoze nemuzeme secist 1 a string "3"

except ZeroDivisionError as e: # vykona se jen, pokud Exception e typu ZeroDivisionError
    vysledek = 0 # pocitame s delenim nulou, osetrime a jedeme dal

except TypeError as e: # vykona se jen, pokud je Exception e typu TypeError
    vysledek = 666 # z nejakeho duvodu se chceme takto zachovat

# Exception = All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.
except Exception as e: # nejaka jina chyba, se kterou jsme nepocitali, sem zapadnou vsechna ostatni Exception nezachycena vyse
    raise e # vyhodime ji dal, aby se o ni postaral nejaky vyssi blok, nebo proste skoncil program errorem
# pokud bysme chteli chytit fakt vsechny vyjimky, meli bysme pouzit except BaseException as e

print(zprava)
```

Příklad nahoře nedává moc smysl - minimálně sčítání čísla a stringu bysme měli ideálně řešit spíš konverzí stringu "3" na int, nebo rovnou napsat `a = random.choice([1, 2.5, 3])`.
Je ale je ukázkou toho, jak díky třídám a dědičnostem můžeme reagovat na určité specifické chyby a zacházet s nimi různě.
A chytit všechny zbývající chyby, se kterými jsme nepočítali a nejsou specificky zachyceny.

## Examples:
[bestie.py](examples.py)