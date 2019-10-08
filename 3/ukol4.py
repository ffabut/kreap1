while True: # nekonečný cyklus
    print("Nejste robot? Má to dvě kola, řidítka, jezdí se na tom, nesmrdí to a nestojí moc, co to je? Zadejte odpověď a potvrďte enterem:")
    x = input()
    if x == "kolo" or x == "bicykl": # x musí být kolo nebo x musí být bicykl, také jsme mohli použít if-elif
        break

    print("\nŠpatně :( Zkuste to ještě jednou...") # \n je zkratka pro enter v textovém řetězci - vytiskneme tak jeden prázdný řádek navíc a bude to hezčí

print("Gratulace, uhodl(a) jste to!")
