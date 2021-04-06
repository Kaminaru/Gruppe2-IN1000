class Sete:
    def __init__(self):
        self._status = "Ledig"

    def settKjop(self):
        self._status = "Kjøpt"

    def settOpptatt(self):
        self._status = "Opptatt"

    def hentStatus(self):
        return self._status

    def __str__(self):
        return self._status