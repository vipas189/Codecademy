import random

key = 42
encrypted = [
    96,
    95,
    89,
    94,
    75,
    89,
    10,
    83,
    88,
    75,
    10,
    77,
    79,
    88,
    67,
    75,
    95,
    89,
    67,
    75,
    89,
    10,
    78,
    238,
    189,
    89,
    94,
    83,
    94,
    69,
    64,
    75,
    89,
]

filename = "output.txt"
length = len(encrypted)

with open(filename, "wb") as f:
    f.write(b"\x00" * length)

indices = list(range(length))
random.seed(42)
random.shuffle(indices)

with open(filename, "r+b") as f:
    for i in indices:
        f.seek(i)
        f.write(bytes([encrypted[i] ^ key]))
