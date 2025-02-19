def prideti_knyga(pavadinimas, autorius, leidimo_metai, zanras):
    dictionary["pavadinimas"].append(pavadinimas)
    dictionary["autorius"].append(autorius)
    dictionary["leidimo_metai"].append(leidimo_metai)
    dictionary["zanras"].append(zanras)


def atvaizduoti_knygas():
    for x in range(len(dictionary["pavadinimas"])):
        print(
            f"{x+1}: Pavadinimas: {dictionary["pavadinimas"][x]}   Autorius: {dictionary["autorius"][x]}   Leidimo metai: {dictionary["leidimo_metai"][x]}   Zanras: {dictionary["zanras"][x]}"
        )


def ieskoti_knygos(paieska):
    for x in range(len(dictionary["pavadinimas"])):
        if paieska in str(dictionary["pavadinimas"][x]) or paieska in str(
            dictionary["autorius"][x]
        ):
            print(
                f"Pavadinimas: {dictionary["pavadinimas"][x]}   Autorius: {dictionary["autorius"][x]}   Leidimo metai: {dictionary["leidimo_metai"][x]}   Zanras: {dictionary["zanras"][x]}"
            )
        elif x + 1 == len(dictionary["pavadinimas"]):
            print("Tokios knygos nera!!!")
    if len(dictionary["pavadinimas"]) == 0:
        print("Tokios knygos nera!!!")


def istrinti_knyga(arg):
    counter = 0
    for x in dictionary["pavadinimas"]:
        if x == arg or arg == str(counter + 1):
            dictionary["pavadinimas"].pop(counter)
            dictionary["autorius"].pop(counter)
            dictionary["leidimo_metai"].pop(counter)
            dictionary["zanras"].pop(counter)
        counter += 1


dictionary = {"pavadinimas": [], "autorius": [], "leidimo_metai": [], "zanras": []}

while True:
    inputas = input(
        "1. Prideti nauja knyga\n2. Atvaizduoti visu knygu sarasa\n3. Ieskoti knygos\n4. Istrinti knyga\n5. Iseiti is programos\n"
    )
    match inputas:
        case "1":
            i1 = input("Iveskite knygos pavadinima: ")
            i2 = input("Iveskite knygos autoriu: ")
            while True:
                try:
                    i3 = int(input("Iveskite leidimo metus(skaicius be kableliu): "))
                    break
                except:
                    print("Vesi apvalu skaiciu tol kol ivesi normaliai")
            i4 = input("Iveskite knygos zanra: ")
            prideti_knyga(i1, i2, i3, i4)
        case "2":
            atvaizduoti_knygas()
        case "3":
            i10 = input("Iveskite pavadinimo arba autoriaus zodzius paieskai: ")
            ieskoti_knygos((i10))
        case "4":
            i11 = input(
                "Irasykite tikslu knygos pavadinima ar eiles numeri norint ja istrinti is saraso: "
            )
            istrinti_knyga(i11)
        case "5":
            print("Davaice seneliumberiukeriukai")
            break
        case _:
            print("Iveskite tik 1 - 5 skaicius.")
