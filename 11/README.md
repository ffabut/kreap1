# Zajímavé built-in moduly, debug mode v IDLE

## Built-in moduly

Během semestru jsme se seznámili s některými built-in moduly.
Python jich však obsahuje velké množství, jejich kompletní seznam je k nahlédnutí na [Python Module Index](https://docs.python.org/3/py-modindex.html).
Nyní se pokusíme stručně podívat alespoň na některé z nich.
Nejde o pořádné ponoření se do těchto modulů, ale spíše takový inspirativní náhled na to, co Python skrze built-in moduly umožňuje.

### configparser

Modul `configparser` nám umožňuje číst a zapisovat nastavení do config filu, který je lehce čitelný lidmi.
Uživatelky programu si tak mohou nastavení snadno 'potunit' dle své libosti.
Plná dokumentace modulu `configparser` je dostupná na [docs.python.org](https://docs.python.org/3/library/configparser.html#module-configparser).

Jednoduchý příklad programu, který vytvoří config file s defaultními hodnotami, pakliže config file neexistuje, v opačném případě načte hodnoty z config filu:

```python
import configparser, os

config = configparser.ConfigParser()
cfgPath = 'config.ini'

# pokud config file neexistuje, muzeme jej vytvorit s default hodnotami
if not os.path.exists(cfgPath):
  print('Config does not exist. Creating the config now...')
  config.add_section('user')
  config['user']['name'] = 'Jane'
  config['user']['surname'] = 'Austen'
  config.write(open('config.ini', 'w'))
  print('Config created at:', cfgPath)

else: # v opacnem pripade precteme hodnoty z config filu
  print('Config found. Using values from:', cfgPath)
  config.read(cfgPath)
  sections = config.sections()
  
  print(sections)
  print(config.get('user', 'name'), config.get('user', 'surname'))

  # hodnoty v config filu je samozrejme mozne updatovat i primo z programu
  print("updating the config now...")
  config['user']['name'] = input('Enter your name: ')
  config.write(open('config.ini', 'w'))
  
  print('config updated')
  print(config.get('user', 'name'), config.get('user', 'surname'))
```

### argparse

Modul `argparse` umožňuje to, aby uživatelky a uživatelé našeho programu mohli parametrizovat běh programu.
A to skrze zadávání argumentů a tzv. flagů při volání programu.
Použití je například následující:

```
python3 main.py argument1 argument2 --flag1 hodnota --flag2 hodnota
```

Díky `argparse` tak můžeme umožnit uživatelkám, aby náš program při každém spuštění dělal trochu jinou věc.
Například mohou specifikovat svoje jméno a tím jej můžeme poté oslovovat.

Příklad použití `argparse` na rozvinutém hello world programu:

```python
import argparse

parser = argparse.ArgumentParser(
  description ='Hello world deluxe edition!',
  epilog = 'Just use it!'
  )

# argumenty bez pomlcek jsou tzv. positional arguments - uvadime je v danem poradi po volani programu, jsou povinne:
# python3 main.py name surname
# python3 main.py Jana Dostalova
parser.add_argument('name', help='Specify the name.')
parser.add_argument('surname', help='Specify the surname.')

# argumenty s pomlckou jsou tzv. optional arguments, jsou nepovinne, na jejich poradi nezalezi, specifikujeme je pomoci jejich nazvu a hodnoty
# python3 main.py Jana Dostalova --friends --count 5
# python3 main.py Jana Dostalova --count 5 --friends
# python3 main.py --friends Jana Dostalova --count 5          atd...
parser.add_argument('--friends', action="store_true", help='Use friendly hello?')
parser.add_argument('--count', help='How many times hello should be said.', default=1, type=int)
# muzeme specifikovat i zkracenou variantu argumentu s jednou pomlckou:
parser.add_argument('-v', '--verbose', help='How verbose the program is. (Not implemented yet.)', type=int, default=1)

args = parser.parse_args()

if args.verbose > 1:
  print("ohoho, we gonna be very verbose!")

hello = "Good day, "
if args.friends == True:
  hello = "Hi, "
  
for i in range(args.count):
  print(hello + args.name + " " + args.surname + "!")
```

### cmd

Modul `cmd` umožňuje vytvářet složitější command-line interfacy.
Při spuštění programu se "vnoříme" do námi vytvořeného příkazu a v jeho rámci pak můžeme dokola volat různé podpřípazy, jde o takový vlastní malý shell/termínál/příkazovku s vlastními příkazy.
Kompletní dokumentace je dostupná [zde](https://docs.python.org/3/library/cmd.html#module-cmd).

Příklad:

```python
import cmd, time

# zde definujeme příkaz a jeho podpříkazy, například: "friend joke", "friend support"
class FriendCMD(cmd.Cmd):
  intro = 'Welcome to FriendCMD. Type help or ? to list commands.\n'
  prompt = '(friend) '

  def do_joke(self, arg):
    'Friend tells you a joke.'
    print("Víš, jak se zdraví členky a členové židovské obce v Ostravě?")
    time.sleep(3)
    print("Shalom, pyčo!")

  def do_support(self, arg):
    'Friend tries to support you.' #dokumentační řetězec metody slouží zároveň jako nápověda pro uživatele
    print("Jsem si jistý, že to zvládneš, všchno bude dobré.")

  def do_echoargs(self, arg):
    'Echoes arguments provided after this command.'
    print(arg) # argumenty jsou dostupné jako řetězec
    print(arg.split()) # můžeme je rozdělit podle mezer na seznam jednotlivých argumentů

  def do_exit(self, arg):
    print("Rád jsem tě viděl, tak zatím, měj se :)")
    return True #pokud vrátíme True, pak se cmdloop() ukončí

FriendCMD().cmdloop()
```

## Debug mode v IDLE

Debug mode nám umožňuje spustit náš program řádek po řádku a průběžně sledovat, jaké hodnoty v proměnných máme.
Velmi se to hodí na ladění programu a hledání toho, kde máme chybu.

Debug mode spustíme v interaktivní python konzoli - klikneme na tlačítko debug a v menu vybereme možnost debugger.
Poté se nám vedle interaktivní konzole otevře debuggovací okno.

Při spuštění programu pak neproběhne program celý, ale pouze jeho první řádek.
Abychom se posunuli na další řádek, musíme kliknout na tlačítko `step`.
V okně debuggeru přitom můžeme průběžně sledovat všechny nadefinované proměnné a hodnoty, které v nich jsou uloženy.
