import datetime
import pickle


class Kambarys:
    def __init__(self, numeris, tipas, kaina_parai, ar_uzimtas):
        self.numeris = numeris
        self.tipas = tipas
        self.kaina_parai = kaina_parai
        self.ar_uzimtas = ar_uzimtas


class Rezervacija:
    def __init__(
        self,
        kliento_vardas,
        kliento_pavarde,
        kambario_numeris,
        pradzios_data,
        pabaigos_data,
        bendra_kaina,
    ):
        self.kliento_vardas = kliento_vardas
        self.kliento_pavarde = kliento_pavarde
        self.kambario_numeris = kambario_numeris
        self.pradzios_data = pradzios_data
        self.pabaigos_data = pabaigos_data
        self.bendra_kaina = bendra_kaina * (pabaigos_data - pradzios_data).days


class Viesbutis:
    def __init__(self, pavadinimas, kambariai, rezervacijos):
        self.pavadinimas = pavadinimas
        self.kabmariai = kambariai
        self.rezervacijos = rezervacijos
        self.kambariai = []
        self.klientai = []

    def __str__(self):
        return f"{self.kambariai}\n{self.klientai}"

    def prideti_kambari(self, kambarys: Kambarys):
        dic = {
            "numeris": kambarys.numeris,
            "tipas": kambarys.tipas,
            "kaina_parai": kambarys.kaina_parai,
            "ar_uzimtas": kambarys.ar_uzimtas,
        }
        self.kambariai.append({"numeris": "laikinas"})
        for nr in range(len(self.kambariai)):
            if self.kambariai[nr]["numeris"] == kambarys.numeris:
                self.kambariai.remove({"numeris": "laikinas"})
                break
            elif nr == len(self.kambariai) - 1:
                self.kambariai.remove({"numeris": "laikinas"})
                self.kambariai.append(dic)

    def rezervuoti_kambari(self, klientas: Rezervacija):
        dic = {
            "kliento_vardas": klientas.kliento_vardas,
            "kliento_pavarde": klientas.kliento_pavarde,
            "kambario_numeris": klientas.kambario_numeris,
            "pradzios_data": klientas.pradzios_data.strftime("%Y-%m-%d"),
            "pabaigos_data": klientas.pabaigos_data.strftime("%Y-%m-%d"),
            "bendra_kaina": klientas.bendra_kaina,
            "dienu_skaicius": (klientas.pabaigos_data - klientas.pradzios_data).days,
        }
        self.kambariai.append({"numeris": "laikinas"})
        for indexNr in range(len(self.kambariai)):
            if self.kambariai[indexNr]["numeris"] == klientas.kambario_numeris:
                if self.kambariai[indexNr]["ar_uzimtas"]:
                    continue
                self.kambariai.remove({"numeris": "laikinas"})
                self.kambariai[indexNr]["ar_uzimtas"] = True
                self.klientai.append(dic)
                break
            elif indexNr == len(self.kambariai) - 1:
                self.kambariai.remove({"numeris": "laikinas"})
                print("Tokio kambario nera, arba uzimtas")
                return

    def atlaisvinti_kambari(self, kambario_numeris):
        self.kambariai.append({"numeris": "laikinas"})
        for x in range(len(self.kambariai)):
            if self.kambariai[x]["numeris"] == kambario_numeris:
                if not self.kambariai[x]["ar_uzimtas"]:
                    continue
                self.kambariai.remove({"numeris": "laikinas"})
                self.kambariai[x]["ar_uzimtas"] = False
                break
            elif x == len(self.kambariai) - 1:
                self.kambariai.remove({"numeris": "laikinas"})
                print("Tokio kambario nera arba jis jau laisvas.")
                return
        for numeris, _ in enumerate(self.klientai):
            if self.klientai[numeris]["kambario_numeris"] == kambario_numeris:
                self.klientai.pop(numeris)

    def isaugoti_i_faila_failu_sistem(self):
        with open("rezervacijos/kambariai.pickle", "wb") as file:
            pickle.dump(self.kambariai, file)
        with open("rezervacijos/klientai.pickle", "wb") as file2:
            pickle.dump(self.klientai, file2)

    def nuskaityti_is_failo_failu_sistema(self):
        try:
            with open("rezervacijos/kambariai.pickle", "rb") as file:
                self.kambariai = pickle.load(file)
            with open("rezervacijos/klientai.pickle", "rb") as file2:
                self.klientai = pickle.load(file2)
        except:
            with open("rezervacijos/kambariai.pickle", "wb") as file:
                pickle.dump(self.kambariai, file)
            with open("rezervacijos/klientai.pickle", "wb") as file2:
                pickle.dump(self.klientai, file2)


k420 = Kambarys(420, "Dvivietis", 110, False)
k520 = Kambarys(520, "Vienvietis", 50, False)
k320 = Kambarys(320, "Liuksas", 400, False)

rezerv420 = Rezervacija(
    "Raimis",
    "Juodauskas",
    420,
    datetime.datetime(2024, 1, 2),
    datetime.datetime(2024, 1, 4),
    110,
)
rezerv520 = Rezervacija(
    "Raimis",
    "Juodauskas",
    520,
    datetime.datetime(2024, 2, 1),
    datetime.datetime(2024, 3, 1),
    50,
)
rezerv320 = Rezervacija(
    "Raimis",
    "Juodauskas",
    320,
    datetime.datetime(2025, 1, 1),
    datetime.datetime(2025, 1, 3),
    400,
)

viesbutis = Viesbutis("Rimgailes", [520, 420, 320], [])

viesbutis.prideti_kambari(k420)
viesbutis.rezervuoti_kambari(rezerv420)
viesbutis.prideti_kambari(k520)
viesbutis.atlaisvinti_kambari(420)

print(viesbutis)
