def haha(*args):
    return max(args)


print(haha(2, 4, 1, 10, 1))


def atbulai(string):
    return string[::-1]


print(atbulai("ka yra"))


def dideles(zodis):
    upperCounter = 0
    lowerCounter = 0
    for raide in zodis:
        if raide.isupper():
            upperCounter += 1
        if raide.islower():
            lowerCounter += 1
    return upperCounter, lowerCounter


print(dideles("asdfjIfasdfF Kjsadf"))


def unikalios(reiksme):
    return set(reiksme)


print(unikalios(["labas", "labas", "hash", "dasdf"]))


def pirminis(sk):
    if sk <= 1:
        return print("ne pirminis")
    for i in range(2, sk):
        if sk % i == 0:
            return print("ne pirminis")
    return print("pirminis")


pirminis(7)


def stringas(sakinys):
    splitintas = sakinys.split()[::-1]
    return " ".join(splitintas)


string = "as esu labai geras vaikas"
print(stringas(string))


# def keliamieji(metai):
for x in range(2, 11):
    print(x)
