"""
Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa.
Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které
filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku a u seriálů
počet episod a délku jedné episody.

Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr.
Oba atributy nastav ve funkci __init__(), žánr získej jako parametr funkce.
Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
Všem třídám přidej funkci get_info(), která vypíše informace o položce, resp. o filmu a seriálu.
Funkce u třídy Polozka vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd Film
a Serial a přidej k ní informaci o délce, resp. počtu episod.
Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál o ověr, že vše funguje.
"""

class Polozka:
  def getInfo(self):
    return f"{self.nazev} je ze žánru {self.zanr}."
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr

class Film(Polozka):
  def getInfo(self):
    return f"Film {super().getInfo()} Je {self.delka} minut dlouhý."
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka

class Serial(Polozka):
  def __init__(self, nazev, zanr, epizody, delkaEpizody):
    super().__init__(nazev, zanr)
    self.epizody = epizody
    self.delkaEpizody = delkaEpizody
  def getInfo(self):
    return f"Serial {super().getInfo()} Má {self.epizody} epizod a kazda epizoda je {self.delkaEpizody} minut dlouha."


pol = Polozka("Star wars", "Sci-fi")
fil = Film("The boat that rocked", "British comedy", 150)
ser = Serial("Red dwarf", "Sci-fi", 57, 25)

print(pol.getInfo())
print(fil.getInfo())
print(ser.getInfo())

