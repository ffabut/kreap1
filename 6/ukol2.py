## Program na procvicovani anglictiny :D

slovicka = {
    "atelier": "studio",
    "umeni": "art",
    "malba": "painting",
    "hra": "game",
    "krajta": "python"
}

for key in slovicka:
    tip = input(key + " je anglicky? ")
    if tip == slovicka[key]: # pokud se tip rovna hodnote ulozene pod klicem
        print("spravne!") #pak vypiseme, ze je to spravne
    else: #v opacnem pripade
        print("spatne!", key, "se anglicky rekne", slovicka[key])

print("a to je vse!")
