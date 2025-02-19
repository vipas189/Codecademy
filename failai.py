from datetime import datetime
import pickle

text = """Zen of Python

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let's do more of those!
"""

with open("Tekstas.txt", "w") as failas:
    failas.write(text)

    # with open("Tekstas.txt", "r") as failas:
    # print(failas.read())

today_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
with open("Tekstas.txt", "a") as failas:
    failas.write(f"\n{today_date}")

"""with open("Tekstas.txt", "r+") as failas:
    array = []
    lineNr = 1
    for line in failas:
        if line == "\n":
            array.append(line)
        else:
            array.append(f"{lineNr} {line}")
            lineNr += 1
    failas.seek(0)
    failas.truncate(0)
    failas.writelines(array)"""

with open("haha.pkl", "rb+") as failas:
    pickle.dump(234, failas)
with open("haha.pkl", "rb+") as failas:
    print(pickle.load(failas))


# # Pakeisime eilutę "Beautiful is better than ugly." į "Gražu yra geriau nei bjauru."
# with open(filename, "r") as f:
#     lines = f.readlines()

# # Modifikuojame atitinkamą eilutę
# lines = [line.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.") for line in lines]

# # Išrašome į failą su pakeista eilute
# with open(filename, "w") as f:
#     f.writelines(lines)

# # Atspausdiname failo turinį atbulai
# with open(filename, "r") as f:
#     content_reversed = f.read()[::-1]
#     print("\nFailo turinys atbulai:\n", content_reversed)

# # Suskaičiuosime žodžius, skaičius, didžiąsias ir mažąsias raides
# words = sum([line.split() for line in lines], [])
# word_count = len(words)
# digit_count = sum(c.isdigit() for c in "".join(words))
# uppercase_count = sum(c.isupper() for c in "".join(words))
# lowercase_count = sum(c.islower() for c in "".join(words))

# print(f"\nŽodžių skaičius: {word_count}")
# print(f"Skaičių skaičius: {digit_count}")
# print(f"Didžiųjų raidžių skaičius: {uppercase_count}")
# print(f"Mažųjų raidžių skaičius: {lowercase_count}")

# # Nukopijuosime visą tekstą į naują failą DIDŽIOSIOMIS RAIDĖMIS
# with open("Tekstas_didziomis.txt", "w") as f:
#     f.write(file_content.upper())
