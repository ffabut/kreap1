class klauzura:
    """
    trida klauzura obsahuje popis dila a moznost jej hodnotit.
    """
    def __init__(self):
        """
        init funkce s interaktivnim vkladanim dat
        """
        self.jmeno = input("Jake je jmeno autorky/autora? ")
        self.nazev = input("Jaky je nazev prace? ")
        self.rok = int(input("Rok vzniku dila? "))
        self.medium = input("Medium, v nemz je dilo vytvoreno? ")
        self.znamka = None # znamku zadame pozdeji

    def show(self):
        """
        Funkce show() prehledne vypisuje data ulozena v objektu klauzura.
        """
        print("=========================")
        print("Název díla:", self.nazev)
        print("Jméno autora/ky:", self.jmeno)
        print("Rok vzniku:", self.rok)
        print("Médium:", self.medium)
        print("Známka:", self.znamka)
        print("=========================")

    def hodnotit(self):
        """
        funkce pro komisi, ktera slouzi k zadavani vysledneho hodnoceni
        """
        self.znamka = input('Zadejte znamku pro dilo "' + self.nazev + '": ')

myFirstArtWork = klauzura()
myFirstArtWork.show() # vse zadano dobre?

# zde prichazi komise
myFirstArtWork.hodnotit()
myFirstArtWork.show() # vysledek
