from emne import Emne
from dato import Dato
from aktivitet import Aktivitet
from student import Student

class Undervisningsadministrasjon:
    def __init__(self):
        self._emner = {} # "IN1000" : Emne objekt
        self._datoer = {} # 200513 : Dato objekt
        self._studenter = {} # "brukernavn" : Student objekt

    def lesFraFil(self, filnavn):
        fil = open(filnavn, "r")
        for linje in fil:
            innhold = linje.strip().split(" ")
            emneKode = innhold[0]
            aktivitet = innhold[1]
            aar = innhold[2]
            maaned = innhold[3]
            dag = innhold[4]

            if emneKode not in self._emner:
                nyEmne = Emne(emneKode)
                self._emner[emneKode] = nyEmne

            absVerdi = int(aar + maaned + dag)
            if absVerdi not in self._datoer:
                nyDato = Dato(dag, maaned, aar)
                self._datoer[absVerdi] = nyDato

            nyAktivitet = Aktivitet(self._emner[emneKode], self._datoer[absVerdi], int(aktivitet[-1]))
            self._emner[emneKode].leggAktivitet(nyAktivitet)

        fil.close()

    def lesStudentFil(self, filnavn):
        fil = open(filnavn, "r")
        for linje in fil:
            innhold = linje.strip().split(" ")
            brukernavn = innhold[0]
            emneKode = innhold[1]
            aktNum = int(innhold[2][-1])

            if brukernavn not in self._studenter:
                nyStudent = Student(brukernavn)
                self._studenter[brukernavn] = nyStudent

            self._emner[emneKode].hentBestemtAktivitet(aktNum).leggTilRegistretStudent(self._studenter[brukernavn])

        fil.close()

    def skrivGrupperMedLavtOppmoete(self, antall):
        for emneNavn in self._emner: # emneNavn is key
            for aktivitet in self._emner[emneNavn].hentAktiviteterListe():
                if aktivitet.oppmote() < antall:
                    print(aktivitet)

