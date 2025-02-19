import datetime as dt
import json


class Kambarys:

    def __init__(self, numeris, tipas, kaina_parai, ar_uzimtas):
        self.numeris = numeris
        self.tipas = tipas
        self.kaina_parai = kaina_parai
        self.ar_uzimtas = ar_uzimtas


class Rezervacija:

    def __init__(self, klnt_vds, klnt_pvrd, kmbr_nr, pradz_dt, pbgs_dt, bendr_kn):
        self.klnt_vds = klnt_vds
        self.klnt_pvrd = klnt_pvrd
        self.kmbr_nr = kmbr_nr
        self.pradz_dt = pradz_dt
        self.pbgs_dt = pbgs_dt
        self.bendr_kn = bendr_kn * ((pbgs_dt - pradz_dt).days)

    def __str__(self):
        return json.dumps(
            {
                "Vardas": self.klnt_vds,
                "Pavarde": self.klnt_pvrd,
                "Nr": self.kmbr_nr,
                "PrdzData": self.pradz_dt,
                "PbgsData": self.pbgs_dt,
                "Kaina": self.bendr_kn,
            },
            indent=4,
        )


class Viesbutis:
    def __init__(self, pavadinimas, kambariai, rezervacijos):
        self.pavadinimas = pavadinimas
        self.kambariai = kambariai
        self.rezervacijos = rezervacijos
        self.array_room = []

    def prideti_kambari(self, kambarys: Kambarys):
        data: dict = {
            str(kambarys.numeris): {
                "Tipas": kambarys.tipas,
                "Kaina": kambarys.kaina_parai,
                "Uzimtumas": kambarys.ar_uzimtas,
            }
        }
        self.array_room.append(data)

    def rezervuoti_kambari(
        self, kliento_vardas, kliento_pavarde, tipas, prad_data, pab_data
    ):
        pass

    def atlaisvinti_kambari(self, kambario_numeris):
        content = self.nuskaityti_is_failo_failu_sistema("rezervacijos/kambariai.json")
        if f"Kambarys: {str(kambario_numeris)}" in content:
            print("yra")

    def issaugoti_i_faila_failu_sistema(self, file_path):
        with open(file_path, "w") as file:
            json.dump(self.array_room, file, indent=4)

    def nuskaityti_is_failo_failu_sistema(self, file_path):
        with open(file_path, "r+") as file:
            content = file.read()
        return content


kmbrs420 = Kambarys(420, "Dvivietis", 50, False)
kmbrs520 = Kambarys(520, "Vienvietis", 30, False)
kmbrs720 = Kambarys(720, "Liuksas", 405, True)

klientas1 = Rezervacija(
    "Adomas", "Laukinis", 420, dt.date(2025, 2, 8), dt.date(2025, 4, 20), 30
)
klientas2 = Rezervacija(
    "Juozas", "Gaidjurgis", 520, dt.date(2025, 2, 3), dt.date(2025, 2, 28), 50
)
klientas3 = Rezervacija(
    "Rimas", "Gruzas", 720, dt.date(2025, 1, 31), dt.date(2025, 2, 5), 70
)
array_client = [klientas1, klientas2, klientas3]

viesbutis = Viesbutis(
    "Augalines", [kmbrs420, kmbrs520, kmbrs720], [klientas1, klientas2, klientas3]
)
viesbutis.prideti_kambari(kmbrs420)
viesbutis.prideti_kambari(kmbrs520)
viesbutis.prideti_kambari(kmbrs720)

viesbutis.issaugoti_i_faila_failu_sistema("rezervacijos/kambariai.json")
viesbutis.atlaisvinti_kambari(420)
