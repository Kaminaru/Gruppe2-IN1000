from hytte import Hytte
from tur import Tur
class Turplanlegger:
    def __init__(self, fil1, fil2):
        self._hytter = self._hytterFraFil(fil1) # ordbok
        self._turer = self._turerFraFil(fil2) # liste

    def _hytterFraFil(self, filnavn):
        ordbok = {} # "hyttenavn" : Hytte objekt
        fil = open(filnavn, "r")
        for linje in fil:
            linjeData = linje.strip().split(" ")
            hyttenavn = linjeData[0]
            antSenger = int(linjeData[1])
            pris = float(linjeData[2])

            nyHytte = Hytte(hyttenavn, antSenger, pris)
            ordbok[hyttenavn] = nyHytte

        fil.close()
        return ordbok

    def _turerFraFil(self, filnavn):
        turListe = []
        fil = open(filnavn, "r")
        linje = fil.readline().strip() # beskrivelse
        while linje != "":
            linjeTo = fil.readline().strip()
            hytteNavner = linjeTo.split()

            hytteObjListe = []
            for navn in hytteNavner:
                hytteObjListe.append(self._hytter[navn])

            nyTur = Tur(hytteObjListe, linje) # linje = beskrivelse
            turListe.append(nyTur)

            linje = fil.readline().strip() # neste beskrivelse

        return turListe

    def finnTurer(self, antP, maksB, maksD) :
        for tur in self._turer:
            if (tur.hentAntHytter() <= maksD and tur.sjekkPrisPlass(antP, maksB)) :
                tur.skrivTur()

def hovedprogram() :
    turplaner = Turplanlegger("hytter.txt", "turer.txt")
    turplaner.finnTurer(7, 7000, 5)

hovedprogram()
