from ukedag import Ukedag
class Ukeplan:
    def __init__(self, hvem):
        self._hvem = hvem # string (persons navn)
        self._ukedager = self.addWeekDays() # liste med ukedager objekter

    def addWeekDays(self):
        liste = []                      # indekser
        liste.append(Ukedag("Mandag"))  # 0
        liste.append(Ukedag("Trisdag")) # 1
        liste.append(Ukedag("Onsdag"))  # 2
        liste.append(Ukedag("Torsdag")) # 3
        liste.append(Ukedag("Fredag"))  # 4
        liste.append(Ukedag("Lørdag"))  # 5
        liste.append(Ukedag("Søndag"))  # 6
        return liste

    def travleste(self):
        dagMedFlestAkt = 0 # indeks i ukedager liste
        for i in range(7):
            if self._ukedager[i].antall() > self._ukedager[dagMedFlestAkt].antall():
                dagMedFlestAkt = i
        return self._ukedager[dagMedFlestAkt]

    def skrivUt(self):
        print(f"Ukeplan for {self._hvem}:")
        for ukedagObj in self._ukedager:
            print(ukedagObj)

    def hentUkedagListe(self):
        return self._ukedager
