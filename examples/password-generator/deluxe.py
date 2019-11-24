"""
Program generuje hesla.
Umožňuje zadat délku hesla, i počet vygenerovaných hesel - aby si uživatelka mohla vybrat to nejlepší.
"""

import random # importujeme modul random

def generatePassword(delka):
  """
  Funkce generuje hesla. Argument "delka" urcuje delku hesla.
  Funkce vraci vygenerovane heslo (type string).
  """

  password = "" # promenna, do ktere budeme postupne ukladat vygenerovane znaky

  for x in range(delka):  # cyklus se zopakuje tolikrat, jak je nastaveny argument delka
   a = random.randint(33, 126) # pomoci funkce randint() z modulu random generujeme nahodna cisla v rozmezi 33 az 126
   password = password + chr(a) # pomoci funkce chr() prevedeme cislo na jemu odpovidajici znak a pridame jej do promenne password
  
  return password # funkce vraci heslo

def genPasses(pocet, delka):
  """
  Funkce generuje zadany pocet hesel o dane delce.
  Prijima argument pocet a delka a vraci seznam textovych retezcu - seznam hesel.
  """
  seznam = []

  for i in range(pocet): # cyklus se provede tolikrat, kolik je pocet - i nepotrebujeme, mohli bychom jej nahradit podrzitkem _
# for _ in range(pocet): 
    heslo = generatePassword(delka) # funkce genPasses vola funkci generatePassword, ktera vygeneruje jedno heslo
    seznam.append(heslo) # heslo se prida do seznamu

  return seznam # funkce vraci seznam hesel
 
# Zde konci definice funkci a defacto zacina program
# vstup uzivatelky
delka = int(input("JAK DLOUHE HESLO?  "))
pocet = int(input("KOLIK HESEL?  "))

# volame funkci genPasses, ktera v sobe pocet-krat vola funkci generatePassword, a nakonec vrati seznam hesel
vysledek = genPasses(pocet, delka)

# vypiseme hesla ze seznamu...
for heslo in vysledek:
  print(heslo)
