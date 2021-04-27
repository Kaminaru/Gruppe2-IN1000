class Emne:
    def __init__(self, emnekode):
        self._aktiviteter = []
        self._emnekode = emnekode

    def leggAktivitet(self, aktivitet):
        self._aktiviteter.append(aktivitet)

    def hentEmnekode(self):
        return self._emnekode
