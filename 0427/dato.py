class Dato:
    def __init__(self, dag, maaned, aar):
        self._dag = dag
        self._maaned = maaned
        self._aar = aar

    def absoluttDato(self):
        absDato = ""
        absDato += str(self._aar)

        if self._maaned < 10:
            absDato += "0" + str(self._maaned)
        else:
            absDato += str(self._maaned)

        if self._dag < 10:
            absDato += "0" + str(self._dag)
        else:
            absDato += str(self._dag)
        return int(absDato)

    def __str__(self):
        datoStreng = str(self._dag) + ". "

        if self._maaned == 9:
            datoStreng += "september "
        elif self._maaned == 10:
            datoStreng += "oktober "
        elif self._maaned == 11:
            datoStreng += "november "
        elif self._maaned == 12:
            datoStreng += "desember "

        datoStreng += "20"
        if self._aar < 10:
            datoStreng += "0" + str(self._aar)
        else:
            datoStreng += str(self._aar)

        return datoStreng

#nyDato = Dato(25,11,20)
# print(nyDato.absoluttDato()) #201119
# print(nyDato)
