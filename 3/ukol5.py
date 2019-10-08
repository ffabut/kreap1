print("Zadejte řetězec a potvrďte enterem.")
text = input()


newText = "" # vytvorime si novou prazdnou promennou, do ktere budeme ukladat souhlasky
# newText musi byt mimo cyklus, jinak by po ukonceni cyklu ztratila platnost - byla vymazana a nemohli bychom se k ni dostat

for znak in text:
    if znak == "a":
        pass # pokud je znak a, pak nebudeme nic delat
    elif znak == "e":
        pass # misto pass jsme v tomto pripade klidne mohli pouzit continue
    elif znak == "i":
        pass
    elif znak == "o":
        pass
    elif znak == "u":
        pass
    elif znak == "y":
        pass
    else: # pokud znak nebyl aeiouy, pak je souhlaskou
        newText = newText + znak # a tak ho ulozime do promenne newText

print(newText)
