from ukeplan import Ukeplan
class Familie:
    def __init__(self):
        self._ukeplaner = [] # liste med ukeplaner objekter

    def leggTilUkeplan(self, hvem):
        self._ukeplaner.append(Ukeplan(hvem))

    def skrivAktiviteter(self):
        # Sol 1
        atkBeskrivelseListe = []
        for ukeplanObjk in self._ukeplaner:
            for ukedagObj in ukeplanObjk.hentUkedagListe():
                for aktivitetsObj in ukedagObj.hentAktListe():
                    if aktivitetsObj != None:
                        aktBeskrivelse = aktivitetsObj.hentAktivitetsNavn()
                        if aktBeskrivelse not in atkBeskrivelseListe:
                            print(aktBeskrivelse)
                            atkBeskrivelseListe.append(aktBeskrivelse)

        # Sol 2
        # aktBesList = []
        # for ukeplanerObj in self._ukeplaner:
        #     for ukedagObj in ukeplanerObj.hentUkedager():
        #         for aktivitetObj in ukedagObj.hentAktiviteter():
        #             if aktivitetObj != None:
        #                 aktBesList.append(aktivitetObj.hentNavn())
        #
        # for aktivitetBeskrivelse in set(aktBesList):
        #     print(aktivitetBeskrivelse)
