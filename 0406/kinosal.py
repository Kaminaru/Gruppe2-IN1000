from sete import Sete
class Kinosal:                         # Kol
    def __init__(self, antallRader, seterPerRad):
        self._seterPerRad = seterPerRad
        self._antallRader = antallRader
        self._kinoSal = self.lagSal()

    def lagSal(self):
        sal = []
        for radNmr in range(self._antallRader):
            tempList = []
            for kolNmr in range(self._seterPerRad):
                nySete = Sete()
                tempList.append(nySete)
            sal.append(tempList)
        return sal

    def kjopBilletter(self):
        for radNmr in range(self._antallRader):
            for kolNmr in range(self._seterPerRad):
                if self._kinoSal[radNmr][kolNmr].hentStatus() == "Ledig":
                    self._kinoSal[radNmr][kolNmr].settKjop()
                    naboListe = self.hentNaboer(radNmr,kolNmr)
                    for nabo in naboListe:
                        nabo.settOpptatt()

    def hentNaboer(self, rad, kol):  # 1 , 1
        """returnerer liste med naboer til bestemt rad og kol nmr."""
        naboListe = []
        for i in range(-1, 2): # rad "naboer" : i = -1, 0, 1
            for j in range(-1, 2): # kol "naboer" : j = -1, 0, 1
                naboRad = rad + i
                naboSete = kol + j
                gyldig = True

                if i == 0 and j == 0:
                    gyldig = False

                # sjekk Rader
                if naboRad < 0 or naboRad >= self._antallRader:
                    gyldig = False

                # sjekk Kol
                if naboSete < 0 or naboSete >= self._seterPerRad:
                    gyldig = False

                if gyldig == True:
                    naboListe.append(self._kinoSal[naboRad][naboSete])

        return naboListe

    def __str__(self):
        tekst = ""
        for rad in self._kinoSal:
            tekst += "|"
            for sete in rad:
                if str(sete) == "Kjøpt":
                    tekst += " KJØPT |"
                else: # ledig, eller "opptatt"
                    tekst += " ----- |"
            tekst += "\n"
        return tekst

