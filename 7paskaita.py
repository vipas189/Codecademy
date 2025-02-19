import datetime

text = """Zen of Python

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Flat is better than nested.
debiliukas
esi
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
In the face of ambiguity, refuse the temptation to guess.
asdfsadf
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let's do more of those!
"""

with open("textas.txt", "w+") as file:
    file.write(text)
    file.write(str(datetime.datetime.today()))
    file.seek(0)
    lines = file.readlines()
    file.seek(0)
    file.truncate(0)
    lineNr = 1
    for line in range(len(lines)):
        if lines[line] == "Beautiful is better than ugly.\n":
            lines[line] = f"{lineNr}. Grazu yra geriau nei bjauru\n"
            lineNr += 1
        elif lines[line] != "\n":
            lines[line] = f"{lineNr}. {lines[line]}"
            lineNr += 1
    file.writelines(lines)
    file.seek(0)
    print(file.read()[::-1])
    zodziai, sk, didz, maz = 0, 0, 0, 0
    for letter in file.read():
        if letter.isupper():
            didz += 1
        elif letter.islower():
            maz += 1
        elif letter.isdigit():
            sk += 1
    file.seek(0)
    eilNr = 1
    for word in file.read().split():
        if word == f"{eilNr}.":
            sk += 1
            continue
        zodziai += 1
    print(f"{zodziai} zodziai, {sk} skaiciai, {didz} dideles raid, {maz} mazos raid")
    file.seek(0)
    with open("textas2.txt", "w+") as file2:
        file2.write(file.read().upper())
