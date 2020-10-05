x = input("zadejte cislo: ")
y = input("zadejte druhe cislo: ")

# pozor: input() vraci zadane hodnoty jako str
# musime prvne konvertovat na float/integer
x = float(x)
y = float(y)

print("soucet je:", x + y)
print("rozdil je:", x - y)
print("soucin je:", x * y)
print("podil je:", x / y)
