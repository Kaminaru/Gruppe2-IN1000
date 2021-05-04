class Aktivitet:
    def __init__(self, hva, kl):
        self._aktNavn = hva # string
        self._start = kl # int

    def hentAktBesk(self):
        return f"Kl {self._start}: {self._aktNavn} "

    def hentAktivitetsNavn(self):
        return self._aktNavn