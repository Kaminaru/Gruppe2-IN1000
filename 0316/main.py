from produkt import Produkt
from butikk import Butikk

def main():
    # Produkter:

    # eple = Produkt("Eple", 3.00, 30) # navn, pris, antall
    # navn = eple.hentNavn()
    # print(navn)
    # eple.selgeProdukt(5)
    # eple.selgeProdukt(50)
    # eple.sjekkAntall()

    # Butikk:
    # butikk1 = Butikk("Kiwi")
    # print(butikk1)
    # eple = Produkt("Eple", 3, 30)
    # butikk1.leggTilProdukt(eple)
    # butikk1.visAlleProdukter()
    # butikk1.produkterFraFil("produkter.txt")
    # butikk1.visAlleProdukter()
    # butikk1.skalSelges("Eple", 5)



    butikk1 = Butikk("Kiwi")
    eple = Produkt("Eple", 3, 30)

    butikk1.leggTilProdukt(eple)
    butikk1.produkterFraFil("produkter.txt")
    butikk1.visAlleProdukter()


main()