from produkt import Produkt

class Butikk:
    def __init__(self, navn):
        self._navn = navn
        self._produkter = []

    def __str__(self):
        return f"Butikkens navn: {self._navn}"

    def leggTilProdukt(self, produkt): # produkt er objekt av Produkt
        self._produkter.append(produkt)
        print(f"Produktet {produkt} er lagt til")

    def visAlleProdukter(self):
        print("Produkter:")
        num = 0
        for prod in self._produkter:
            num += 1
            print(str(num) + ".", prod)

    def produkterFraFil(self, filnavn):
        fil = open(filnavn, "r")
        for linje in fil:
            linjeListe = linje.strip().split(",")
            navn = linjeListe[0]
            pris = float(linjeListe[1])
            antall = int(linjeListe[2])

            nyProd = Produkt(navn, pris, antall)
            self._produkter.append(nyProd)
            #self.leggTilProdukt(nyProd)
        fil.close()
        print(f"Produkter fra fil: {filnavn} er lagt til butikken")

    def skalSelges(self, produktNavn, antall):
        for produkt in self._produkter:
            if produkt.hentNavn() == produktNavn:
                produkt.selgeProdukt(antall)