def multipleHello(jmeno, x=1):
    pozdrav = "Hello " + jmeno + "!" # pozdrav vytvorime zde, at to pocitac nemusi vypocitavat pri kazdem novem pozdravu
    while x > 0:
        print(pozdrav)
        x = x - 1 # po pozdraveni zmensime x o 1 a cyklus se pote zepta, zda je cislo stale vetsi nez 0, tj. jestli mame jeste jednou opakovat
    # navratova hodnota neni treba

# test zda to funguje:
multipleHello("Eve", 9)
multipleHello("George") # pokud nebudeme specifikovat druhy parametr, pouzije se jeho vychozi hodnota
