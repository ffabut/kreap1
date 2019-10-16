def func1(a):
    print("tady funkce1, a je:", a)
    func2(a/2) # funkce1 vola funkci2

def func2(x):
    print("tady funkce2, x je:", x)
    func1(x*2 + 30) # ale funkce2 vola zpet funkci 1 - tohle bychom nemeli delat

# tady odstartujeme nekonecne volani funkci sebe navzajem
# jedna se o tzv. rekurzi, ktera muze byt obcas uzitecna, je vsak treba ji kontrolovat a vedome uzivat
# tady ji nechame bezet bez kontroly, dokud to python snese a pak spadne
func1(1)
