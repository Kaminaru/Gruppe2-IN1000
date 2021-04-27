class Tur:
    def __init__(self, hytterListe, beskrivelse):
        self._hytterListe = hytterListe
        self._beskrivelse = beskrivelse

    def skrivTur(self):
        print(self._beskrivelse)
        for hytte in self._hytterListe:
            print(hytte)

    def sjekkPrisPlass(self, antallPer, maksBelop):
        totalPris = 0
        for hytte in self._hytterListe:
            if hytte.sjekkPlass(antallPer) == False:
                return False
            totalPris += hytte.totPris(antallPer)
            if totalPris > maksBelop:
                return False
        return True




