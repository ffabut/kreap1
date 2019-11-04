## Program, který zjišťuje, zda má uživatelka podobný vkus na umělkyně jako autorka programu.

mojeOblibeneUmelkyne = (
    "Christian Falsneas",
    "Markéta Wágnerová",
    "Jeremy Deller",
    "Hans Haacke",
    "Ládví",
    "WochenKlausur"
)

jejiOblibena = input("Zadejte vasi oblíbenou umělkyni nebo umělce: ") # pokud do input() zadáme jako parametr řetězec,
# tak se použije jako výzva před zadáním textu od uživatelky

if jejiOblibena in mojeOblibeneUmelkyne: # není ideální - ještě bychom měli porovnávat velká a malá písmena, ale to až někdy příště...
    print("Hurá! Máme stejnou oblíbenou umělkyni:", jejiOblibena)
else:
    print("Tak to nevim.")
