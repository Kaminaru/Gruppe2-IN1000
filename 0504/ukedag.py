from aktivitet import Aktivitet
class Ukedag:
    def __init__(self, dag):
        self._dag = dag # String (Mandag, Trisdag ...)
        self._aktiviteter = [] # maks 24 elementer

        for i in range(24): # i fra 0 til 23
            self._aktiviteter.append(None)

       #  [None,None,None, None, None, Aktivitet Objekt,  ....]

    def hentAktListe(self):
        return self._aktiviteter

    def settInn(self, hva, kl): # kl fra 0 til 23
        if self._aktiviteter[kl] == None:
            self._aktiviteter[kl] = Aktivitet(hva, kl)
        else: # self._aktivitet[kl] != None
            print("Klokkeslett er optatt!")

    def tidligste(self):
        for i in range(24): # fra 0 til 23
            if self._aktiviteter[i] != None:
                return i
        return -1

    def seneste(self):
        for i in range(23, -1, -1):
            if self._aktiviteter[i] != None:
                return i
        return -1

    def antall(self):
        antallAkt = 0
        for el in self._aktiviteter:
            if el != None:
                antallAkt += 1
        return antallAkt

    def settInnLedig(self, hva):
        if self.antall() == 24:
            print("Kalendaren er full")
        elif self.antall() == 0:
            #self._aktiviteter[12] = Aktivitet(hva, 12)
            self.settInn(hva, 12)
        else:
            if self.seneste() - self.tidligste() > 1:
                for i in range(self.tidligste()+1, self.seneste()):
                    if self._aktiviteter[i] == None:
                        self._aktiviteter[i] = Aktivitet(hva, i)
                        return

            for i in range(self.seneste(), 24):
                if self._aktiviteter[i] == None:
                    self._aktiviteter[i] = Aktivitet(hva, i)
                    return

            for i in range(0, self.tidligste()): # ogsaa mulig (self.tidligste(), -1, -1)
                if self._aktiviteter[i] == None:
                    self._aktiviteter[i] = Aktivitet(hva, i)
                    return

    def __str__(self):
        strengen = self._dag + " "
        for aktivitetObj in self._aktiviteter:
            strengen += aktivitetObj.hentAktBesk()
        return strengen



