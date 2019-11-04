# program kombinuje vsechna slova ze dvou seznamu
# aka generator nazvu

pridavna = ["Post", "Utopian", "Feminist", "Communist", "Activist", "Black", "Terrestrial", "Mediated", "Artificial", "Cyber", "Alt", "Urban"]
podstatna = ["Swarm", "Web", "Utopia", "Protests", "Cybernetics", "Art", "Feminism", "Osterity", "Riots", "Survival", "Biennale"]

result = [] # prazdny slovnik, do ktereho budeme ukladat vysledky

for pridavne in pridavna: # iterace pres seznam pridavne post, utopian, feminist atd...
    # vezmeme slovo z pridavnych jmen
    for podstatne in podstatna: # a projdeme pres vsechna podstatna jmena
        souslovi = pridavne + " " + podstatne
        result.append(souslovi)


print(result)