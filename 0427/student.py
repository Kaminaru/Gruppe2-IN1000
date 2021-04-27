class Student:
    def __init__(self, brukernavn):
        self._emner = []
        self._brukernavn = brukernavn

    def hentBrukernavn(self):
        return self._brukernavn
