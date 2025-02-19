import datetime
class Sukaktis:
    def __init__(self, date):
        self.date = date

    def lastSukaktis(self, date2):
        if date2 % 4 == 0 and (date2 % 100 != 0 or date2 % 400 == 0):
            print("keliamieji")
        else:
            print("nekeliamieji")
        return f"{self.date - date2} "

    def keliamieji(self,)
