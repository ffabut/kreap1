# Hodina 1 - instalace prostředí

Instalace se bohužel na Mac, Linuxu i Windows drobně liší.
Text je proto poněkud delší a komplikovanější, ale relevantní je pro vás vždy jen cca třetina - dle vašeho operačního systému.

## Instalace Python

Pokusíme se nainstalovat programování jazyk Python 3.
Součástí instalace je:
1. textový editor `IDLE` určený k psaní Python kódu
2. interpreter `python` - s jeho pomocí můžeme spouštět pythonové skripty/programy

### Windows
1. instalátor lze stáhnout z <https://www.python.org/downloads/>
2. spusťte stažený instalační soubor
3. v počátku instalace zatrhněte "add Python to PATH" - instalace tak přidá příkaz "python" do "PATH" - operační systém tak bude vědět, kde python hledat a bude možné jej spouštět.
4. vyhledejte program IDLE, případně IDLE3 - editor Python kódu, měl by být nainstalován společně s pythonem
5. otevřete PowerShell (lze vyhledat v nabídce Start) a zadejte příkaz "python --version"   
   1. pokud PS vypíše `Python 3.7.x` je vše v pořádku
   2. pokud PS vypíše `Python 2.x.y`, pak zkuste zopakovat bod 4 s příkazem `python3 --version`, nejspíše je nainstalován i Python 2 a je první na cestěm příkazem python3 to obejdeme, jelikož přesně specifikujeme verzi 3 - pokud vypíše nyní `Python 3.7.x` zadávejte nadále stále `python3` namísto `python`
   3. pokud PS vypíše, že nebylo možné najít python, pak Python nejspíše není na PATH, zeptejte se vyučujícího - nebo zkuste googlit "add python 3 to path on windows"

### Mac OS
1. instalátor lze stáhnout z <https://www.python.org/downloads/>
2. spusťte stažený instalační soubor
3. vyhledejte program IDLE, případně IDLE3 - editor Python kódu, měl by být nainstalován společně s pythonem
4. otevřete program "terminal" - příkazovou řádku, lze najít ve Finderu
5. zadejte příkaz `python --version`
   1. pokud terminal vypíše `Python 3.7.x` je vše v pořádku
   2. pokud terminal vypíše `Python 2.x.y`, pak zkuste zopakovat bod 4 s příkazem `python3 --version`, nejspíše je nainstalován i Python 2 a je první na cestěm příkazem python3 to obejdeme, jelikož přesně specifikujeme verzi 3 - pokud vypíše nyní `Python 3.7.x` zadávejte nadále stále `python3` namísto `python`
   3. pokud PS vypíše, že nebylo možné najít python, pak Python nejspíše není na PATH, zeptejte se vyučujícího - nebo zkuste googlit "add python 3 to path on mac"

### Linux

1. Python3 je často již nainstalovaný, 
   1. otevřete příkazovou řádku
   2. zadejte `python3 --version`, pokud vypíše verzi 3.x.y, je vše v pořádku, máte hotovo
2. Pokud ne, je třeba python nainstalovat pomocí instalátoru vaší distribuce:
   1. Fedora: `sudo dnf install python3`
   2. Ubuntu: `sudo apt-get install python3.6`
3. otestujte příkazem `python3 --version` v terminalu, že je Python nainstalován
   1. pokud terminal vypíše `Python 3.7.x` je vše v pořádku
   2. pokud terminal vypíše `Python 2.x.y`, pak zkuste zopakovat bod 4 s příkazem `python3 --version`, nejspíše je nainstalován i Python 2 a je první na cestěm příkazem python3 to obejdeme, jelikož přesně specifikujeme verzi 3 - pokud vypíše nyní `Python 3.7.x` zadávejte nadále stále `python3` namísto `python`
   3. pokud PS vypíše, že nebylo možné najít python, pak Python nejspíše není na PATH, zeptejte se vyučujícího - nebo zkuste googlit "add python 3 to path on mac"
4. vyhledejte program IDLE, případně IDLE3 - editor Python kódu, měl by být nainstalován společně s pythonem, alternativně lze použít editor vim, emacs nebo nano a skripty spouštět z příkazové řádky
            
### Alternativa: Online Python

Pokud z nějakého důvodu nejde Python nainstalovat, je stále možné použít webové prostředí.
Pěkné Python prostředí nabízí například [repl.it](https://repl.it/):  
1. zaregistrujte se (zdarma)
2. klikněte na `new repl`
3. vyberte jazyk Python
4. můžete začít programovat

## Instalace Git

### Windows

1. Git lze stáhnout z https://git-scm.com/download/win, poté nainstalovat
2. instalace lze ověřit v PowerShellu příkazem: `git --version`

### Mac
1. Přítomnost Gitu lze ověřit příkazem `git --version`
   1. Pokud vypíše `git version x.y.z` je vše ok
   2. v opačném případě se Mac nejspíše zeptát, zda jej nechcete nainstalovat skrze `Xcode Command Line Tools`
   3. alternativně lze instalovat přímo instalačním souborem z: https://git-scm.com/download/mac

### Linux

1. k instalaci užijte instalátor vaší distribuce:
   1. Fedora: `sudo dnf install git-all`
   2. Ubuntu: `sudo apt install git-all`
2. Ověřte instalaci příkazem: `git --version`
