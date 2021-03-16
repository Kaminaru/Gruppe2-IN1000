class Produkt:
    def __init__(self, navn, pris, antall):
        self._navn = navn
        self._pris = pris
        self._antall = antall

    def __str__(self):
        return self._navn

    def hentPris(self):
        return self._pris

    def sjekkAntall(self):
        print(f"Det er {self._antall} {self._navn}(er/r)")

    def hentNavn(self):
        return self._navn

    def selgeProdukt(self, antall):
        if self._antall - antall < 0:
            print(f"Ikke nok {self._navn}(er/r) i butikken")
        else:
            self._antall -= antall
            print(f"Solgt {antall} {self._navn}(er/r)")
