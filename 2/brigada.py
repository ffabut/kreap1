mzda = input("Kolik korun za hodinu dostaneš hrubého? ")
cas = input("Kolik hodin budes makat? ")

mzda = float(mzda)
cas = float(cas)

# az se naucime podminky, muzeme tu zohlednit i slevy na dani atd...
vydelek = mzda * 0.85 * cas

print("výdělek po zdanění bude:", vydelek)
