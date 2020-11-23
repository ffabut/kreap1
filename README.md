# KREAP1 - Kreativní programování 1

Předmět kreativní programování 1 na FaVU VUT v Brně.
Zápisky a materiály k výuce.

## Osnova kurzu

1. [Úvod do kurzu, Instalace](1/README.md)
2. [První program - Hello World, funkce print(), Proměnné, Porovnávání, Logické operátory: nebo, a, negace](2/README.md)
3. [Řídící struktury: Podmínka IF, Cykly WHILE a FOR, klíčová slova continue a break](3/README.md)
4. [Funkce, built-in funkce, tvorba vlastní funkce](4/README.md)
5. [Kolekce - Ntice, Seznamy, Množiny](5/README.md)
6. [Kolekce - Slovníky, některé další operace s kolekcemi](6/README.md)
7. [Import modulu](7/README.md), [Procvicovani: program generujici hesla](examples/password-generator)
8. [Objektově orientované programování: třídy, metody](8/README.md)
9. [Reference](9/README.md)
10. Správa zdrojového kódu, Git, Větvení v Gitu, Github
11. Slovníky, JSON, API
12. Třídy, Dědičnost
13. Závěrečný projekt
14. Závěrečný projekt, retrospektiva

Zápočtový úkol: [informace zde](zapocet/README.md)

## Ukázkový kód

Repositář obsahuje také několik málo ukázkových příkladů kódu.
Ty najdete ve složce [examples](examples/).

## Kreativní programování / Software Art - ukázky

### Náhodný Slušný Čech

Malá webová aplikace "s prvky umělé debility" napsaná v JavaScriptu, která generuje "názory" slušných (xenofobních) Čechů. Dostupné na https://jkremser.github.io/nahodny-slusny-cech/, zdrojový kód potom na: https://github.com/jkremser/nahodny-slusny-cech. Ukázka:

```
NEZISKOVKY tu ZAPLAVUJÍ médija s EUROFAŠIZACÍ a mezitím deseti1000íce PŘIVANDROVALCŮ se sem MLČKY hrne!! NEBUĎTE OVCE.... ČINA a RUSKO JSOU ASPOŇ PRO tuto zemy PŘÍNOS ,což se o TĚCH AGENTECH CIA říct nedá !!! Přece NECHCEME ABY SLUŠNÍ LIDI MUSELY PLATIT JENOM DANĚ a hubu JAK ovce a SOBOTKA, PRAŽSKÁ KAVÁRNA, CIKÁNI aspol. pořád JENOM kradli tohle už ne!!! !!!
```

I přes relativní věrohodnost výstupů se vše odehrává na 340 řádcích kódu, polovinu z nich zabírají komentáře uložené do proměnných, druhou pak funkce generující z komentářů komentáře nové.
Autor není umělec, ale programátor povoláním.
I tak jde ale o velmi povedené angažované dílo.

### Akron & Cincinnati

Akron & Cincinnati z roku 2012 je twitterový bot umělce Coryho Arcangela.
Tento skript v programovacím jazyce Perl automaticky zveřejňuje na Twitter posty v zažitém tvaru `město-->město` a tím předstírá, že vlastník účtu hodně cestuje.
Jde o automatické hraní divadla na sociální síti.

Kód je dostupný z https://github.com/coryarcangel/Akron-Cincinnati/ (ale možná již nebude funkční).
Více o díle je možné najít na portfoliu umělce: http://www.coryarcangel.com/things-i-made/code-akron-cincinnati.

Tento bot by se v současnosti v Pythonu dal napsat za použití knihovny Tweepy (http://www.tweepy.org/).
S Tweepy jde napsat i vlastní, jinak fungující Twitterové boty.

### Pizza Party

Pizza Party z roku 2004 od Coryho Arcangela je program, který umožňuje objednávat pizzu z příkazové řádky.
Dost možná jde o ironický komentář ke všem možným užitečným prográmkům do příkazové řádky - jejich určité zradikalizování a převod do nástroje ovlivňujícího běžný život, nebo možná jen komentář k jisté lenosti části programátorské a IT obce...

Napsáno v Pearlu, kód je dostupný na: https://github.com/coryarcangel/Pizza-Party-0.1.b/, ale program po letech už asi nebude funkční.

### Reject Me

Reject Me z roku 2005 od neznámé autorky pomáhal svým uživatelům udržet své místo na pracovním úřadě v GB.
A to tím, že umožňoval generovat falešné zprávy o odmítnutí uchazeče z pracovního konkurzu.
Více o programu je možné najít na: http://runme.org/project/+rejectme/?fbclid=IwAR256N0RECFkB7rL9mInVwGgnQpkf-ankrErDbVAEZExZBwIHBVLYW3A85E.

## Další zdroje pro studium

Pěkné materiály nabízí česká neziskovka Pyladies.cz, dostupné jsou například zde: https://naucse.python.cz/2019/brno-podzim-pondeli/.
Oproti materiálům kurzu KREAP1 jsou obsáhlejší a dají se použít k dalšímu procvičování.
