class Hytte:
    def __init__(self, navn, antallSenger, pris):
        self._navn = navn
        self._antallSenger = antallSenger
        self._pris = pris

    def hentNavn(self):
        return self._navn

    def totPris(self, antPersoner):
        return antPersoner * self._pris

    def sjekkPlass(self, antPersoner):
        if antPersoner <= self._antallSenger:
            return True
        return False

    def __str__(self):
        svar = self._navn + ". Antall senger: " + str(self._antallSenger) + "\n"
        svar += str(self._pris) + " kr per natt."
        return svar

    def __eq__(self, annenObj):
        return self._navn == annenObj.hentNavn()