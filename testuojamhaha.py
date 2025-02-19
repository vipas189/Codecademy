def f1(array):
    return print(max(array))


array = [1, 5, 3, 2, 1]
f1(array)


def f2(sk):
    if sk % 2 == 0:
        return print("skaicius lyginis")
    elif sk % 2 != 0:
        return print("nelyginis")


f2(3)


def f3(n):
    array = []
    for x in range(1, 11):
        array.append(n * x)
    return array


print(f3(2))


def f4(array):
    return print(set(array))


array = [2, 1, 5, 3, 2]
f4(array)
