from emne import Emne
from dato import Dato

class Aktivitet:
    def __init__(self, emne, dato, aktivitetsnummer):
        self._emne = emne # objekt av emne
        self._dato = dato # objekt av dato
        self._aktNummer = aktivitetsnummer
        self._registrerte = [] # studenter som er registrert paa SW
        self._oppmote = [] # de som faktist har mott opp til denne aktiviteten

    def leggTilRegistretStudent(self, student):
        self._registrerte.append(student)

    def registrerOppmote(self, student):
        self._oppmote.append(student)

    def skrivUtOppmoteStudenter(self):
        for student in self._oppmote:
            print(student.hentBrukernavn())

    def absoluttDato(self):
        return self._dato.absoluttDato()

    def oppmote(self):
        return len(self._oppmote)

    def __str__(self):
        svar = ""
        svar += f"{self._emne.hentEmnekode()} "
        svar += str(self._aktNummer)
        svar += f" {self.oppmote()}"
        return svar



nyemne = Emne("IN1000")
nydato = Dato(2,10,25)
aktivitet = Aktivitet(nyemne, nydato, 2)
# print(aktivitet.absoluttDato())
print(aktivitet)