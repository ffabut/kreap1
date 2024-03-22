
class Bestie():
    zdravi = 100.0
    def scream(self, agressive):
        if agressive:
            print(f"Arrrrgh, I am {self.name} the {self.typ}!!!!!!!!!!")
        else:
            print(f"I am {self.typ} the bestie :)")

    def __init__(self, name, typ="Vlk"):
        self.typ = typ
        self.name = name


class MagickaBestie(Bestie):
    def do_magic(self):
        print(f"I am {self.name} and I am doing magic")


class UndeadBestie(Bestie):
    def rot(self):
        print(f"I am {self.name} and I am rotting")


hydra = MagickaBestie("Hydranta")
skeleton = UndeadBestie("Bony")

vlk = Bestie("Ron")
vlk.Scream(True)

vlk2 = Bestie("Argo")
vlk2.Scream(True)

drak = Bestie("Alfred II.", "Drak")
drak.Scream(False)


