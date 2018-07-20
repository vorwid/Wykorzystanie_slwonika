#Przedstawie uzywanie slownika

geek = {"404":"ignorant; od uzywanego w sieci WWW komunikatu o błedzie 404 - nie znaleziono strony.",
        "Googling":"googlowanie; wyszukiwanie winternecie informacji dotyczacych jakiejs osoby.",
        "Keyboard Plaque":"zanieczyszczenia nagromadzone na klawiaturze komputera.",
        "Link Rot":"proces, w wyniku którego linki do stron WWW staja sie nieaktualne.",
        "Percussive Maintenance": "naprawa urządzenia elektronicznego przez stukniecie."}

choice = None
while choice != "0":
    print(" Translator slangu komputerowego")
    print("""
            0 - zakoncz
            1 - znajdz termin
            2 - dodaj nowy termin
            3 - zmien istniejacy termin
            4 - usun termin

        """)
    choice = input("Wybierasz: ")
    print()
    
    if choice == "0":
        print("Zegnaj")

    elif choice == "1":
        term = input("Jaki termin mam znalezc?")
        if term in geek:
            definition = geek[term]
            print("\n", term, "oznacza", definition)
        else:
            print("Niestety, nie znam terminu", term)

    elif choice == "2":
        term = input("Jaki termin dodac?")
        if term not in geek:
            definition = input("Podaj definicje tego terminu")
            geek[term] = definition
            print("Termin", term,"zostal dodany.")
        else:
            print("Ten termin juz istnieje! Sproboj zmienic jego definicje")

    elif choice == "3":
        term = input("Jaki termin mam przedefiniowac?")
        if term in geek:
            definition = input("Jaka jest nowa definicja?")
            geek[term] = definition
            print("Termin", term,"zostal przedefiniowany")
        else:
            print("Ten termin nie istnieje! Sproboj go dodac")

    elif choice == "4":
        term = input("Jaki termin usunac?")
        if term in geek:
            del geek[term]
            print("Usunalem go", term)
        else:
            print("Terminu nie ma w slowniku")

    else:
        print("Niestety", choice,"to nieprawidlowy wybor")


input("\n\n Aby zakonczy program nacisnij klawisz Enter")
        
