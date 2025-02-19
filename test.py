"""stringas = "Zen of Python"

# Atspausdintu paskutinio antro zodzio simboli (situos darykite su split)
print(stringas.split()[1][-1])

# Atspausdintu pirma trecio zodzio simboli
print(stringas.split()[2][0:1])

# Atspausdintu tik pirma zodi (pameginkite ir su slicing pvz. tekstas[0:5]) ir su split
print(stringas[0:3])
print(stringas.split()[0])

# Atspausdintu tik paskutini zodi
print(stringas.split()[2])

# Atspausdintu visa fraze atbulai
print(stringas[::-1])

# Atskirtu zodzius ir juos Atspausdintu
print(stringas.split())

# Zodi "Python" pakeistu i "Programming" ir atspausdintu nauja sakini
print(stringas.replace("Python", "Programming"))

# Leisti ivesti naudotojui teksta ir atspausdinkite ji atvirksciai
armuha = input("Iveskite belenka seniuk: ")
print(armuha[::-1])


# Leisti vartotojui ivesti metus
while True:
    try:
        metai = int(input("ivesk metus pirikupas: "))
        break
    except ValueError:
        print("vesk tik skaiciu pirikupas")

# Atspausdint "Keliamieji metai", jei taip yra

# Sukurkite sarasa su pasikartojanciomis reiksmemis, viena komanda pasalinkite visas sias pasikartojacias reiksmes
array = [1, 2 ,3 ,3 ,1 ,5, 5, 9, 1, 5, 9]
print(set(array))

# Sukurkite du identiskus objektus (tuple ir sarasas), pamatuokite ar atspausdindami visus tuple elementus sutaupote laiko palyginus su spausdinant visus saraso elementus
import time # as zinau kad importai eina paciam virsuj!!!

start = time.perf_counter()
tuplee = (2, 5, 1, "Labas", 5, 1)
end = time.perf_counter()

start2 = time.perf_counter()
array = [2, 5, 1, "Labas", 5, 1]
end2 = time.perf_counter()
print((end - start)*1000,"\n",(end2 - start2)*1000)


name = input("Iveskite varda: ")
surname = input("Iveskite pavarde: ")
age = input("Iveskite amziu: ")
element4 = input("ivesk beleka seni: ")
element5 = input("BELEKA!!!!: ")

dictionary = {}

dictionary["Name"] = name
dictionary["surname"] = surname
dictionary["age"] = age
"""

array2 = [2, 5, 1, 3]
array2.sort(reverse=True)
sorted_array2 = sorted(array2)
print(array2)

v = {"Vardas:": "rokas", "Pavarde:": "paulauskas", "Metai:": "24"}
k = list(v.items())
print(k[0][0], k[0][1], "\n", "ir taip toliau bet tingejau f naudot")

print(list(v))

dictionary = ["kaktusas", "sukulentas", "sukulentas", "aguona"]

print(set(dictionary))
