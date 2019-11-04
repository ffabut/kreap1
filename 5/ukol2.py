# Hádankový program

variantyJmena = ("Petr Pudil", "petr pudil", "pudil petr", "Pudil Petr", "Pudil", "pudil")

napovedy = (
    "výhodně privatizoval(a)",
    "sbírá umění",
    "většina kolegů z dob privatizace sedí",
    "vlastnil(a) uhelné doly",
    "sponzoroval(a) klauzury AVU dokud AVU nenašla vlastní důstojnost",
    "chtěl(a) žalovat Artyčok za kritický text od Václava Drozda",
    "má ??? Family Foundation",
    "2021 bude v praze otevírat Kunsthalle"
)

print("Zahrajeme si hru. Budu vám dávat nápovědy a vy se budete snažit uhodnout jméno člověka.")
for napoveda in napovedy:
    print(">>>", napoveda, "<<<")
    tip = input("Zadejte Váš tip: ")

    if tip in variantyJmena:
        print("Gratulace, uhodli jste! Je to privatizační umělec Petr Pudil!")
        break # ukonci prubeh cyklem, takze se nebudeme dále ptát
    else:
        print("Nene, zkuste to ještě jednou...")
