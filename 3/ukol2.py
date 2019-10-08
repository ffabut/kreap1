print("Prosím, dokažte, že nejste bot. Jaký je výsledek 'tři plus čest'? Zadejte výsledek a potvrďte enterem.")

vysledek = input() # protentokrat input() neprevedeme na integer, ale nechame jako string - co kdyby uzivatel zadal slovo?

if vysledek == "9": # input() vrací typ string, takze vysledek je typu string a proto je 9 v uvozovkach - abychom porovnavali dva stringy
    print("OK - nejste bot")
elif vysledek == "devět": # kdyby náhodou někdo zadal číslo 9 slovem
    print("OK - nejste bot")
elif vysledek == "devet": # nezapomeneme na lidi s anglickou klavesnici
    print("OK - nejste bot")
else:
    print("FAIL - možná jste bot")
