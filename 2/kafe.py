tydne = input("Ahoj, vitej v Kafkulačce! Kolik cca kafí dáš za týden? ")
tydne = int(tydne) # převod textového řetězce na celé číslo
print()

dekada = tydne * 52 * 10 # 52 tydnu v roce, 10 let
print(f"Za deset let vypiješ přibližně {dekada} kafí! Těch bytů...! 🤡")

gramu = 7 * dekada # 7 gramů kávy v jednom kafi
print()
print(f"To je celkem asi {gramu/1000} kilogramů zrnkové kávy!")

kofeinu = dekada * 63 / 1000 # 63 mg kofeinu v jednom kafi, převod na gramy
print()
print(f"A to dělá asi {kofeinu} gramů naprosto čistého kofeinu!")

