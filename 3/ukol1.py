x = input() # uzivatel zada cislo a to ulozime do promenne X (pozor: input() vraci datovy typ string)
x = int(x) # a proto string prekonvertujeme pomoci funkce int() na cele cislo

if x > 100:
    print("cislo je vetsi nez 100!")

if x < 100:
    print("cislo je mensi nez 100!")

# vsimneme si, ze jsme vlastne nepokryli situaci, kdy x je 100, ale to v zadani nebylo...
    