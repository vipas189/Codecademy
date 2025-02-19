class Sakinys:
    def __init__(self, text):
        self.text = text

    def txtreverse(self):
        return self.text[::-1]

    def txtlower(self):
        return self.text.lower()

    def txtupper(self):
        return self.text.upper()

    def txtrow(self, number):
        return self.text.split()[number]

    def txtSymbolCount(self):
        return f"Zodziai: {len(self.text.split())}\nSymobliai: {len(self.text)}"

    def txtReplace(self, originalTxt, replaceTxt):
        return self.text.replace(originalTxt, replaceTxt)

    def txtCounter(self):
        nr = 0
        low = 0
        up = 0
        for symbol in self.text:
            if symbol.isnumeric():
                nr += 1
            if symbol.islower():
                low += 1
            if symbol.isupper():
                up += 1
        return f"Zodziai: {len(self.text.split())}\nSkaiciai: {nr}\nDidziosios raides: {up}\nMazosios raides: {low}"


sakinys = Sakinys("labas 13 kas tu toks esi Yes")

print(sakinys.txtupper())
