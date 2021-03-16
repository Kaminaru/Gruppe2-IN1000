class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder

    def hentNavn(self):
        return self._navn

    def __str__(self):
        return f"Jeg heter {self._navn}"

    def __eq__(self, annen):
        svar = (self._navn == annen._navn) and (self._alder == annen._alder)
        return svar


person1 = Person("Arthur", 20)
person2 = Person("Daniel", 23)

list = [1,2,3,4]
print(dir(list))

