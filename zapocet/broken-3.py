# program na generování tiskových zpráv

class exhibition:
  institutions = [
    "anna.remesova@artalk.cz"
    "alzbeta.cibulkova@artalk.cz"
    "info@artalk.cz"
  ]

  def __init__(self):
    name = input("Zadejte název výstavy: ")
    gallery = input("V jaké galerii se výstava odehraje? ")
    date = input("Kdy se výstava odehraje? ")
    artists = []
    while True:
      artist = input("Zadejte jméno vystavující umělkyně, nebo umělce (ukončíte pokud nezadáte nic a zmáčknete enter): ")
      if artist == "":
        continue #prerusime cyklus while
      artists.append(artist)

  def generovatTZ():
    print("send TZ to:", self.institutions)
    print("předmět: Zasíláme TZ k výstavě " + self.name)
    artistsString = ""
    if len(self.artists) == 1:
      artistsString = self.artists[0]
    else:
      i = 0
      for artist in self.artists:
        if i == 0:
          artistsString = artist
        else:
          artistsString = artistsString + ", " + artist
        i = i + 1

    print("tělo emailu:", "Srdečně Vás zveme na vernisáž výstavy " + self.name + ", kterou " + self.date + " pořádá " + self.gallery + ". Vystavují: " + self.artList + "." )

exhibition = exhibition()
exhibition.generovatTZ()
