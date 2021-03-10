"""
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 3 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	Peugeot 403 Cabrio	47534
1P3 4747	Škoda Octavia	41253
Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí.
Třída bude mít tyto atributy:

registrační značka automobilu,
značka a typ vozidla,
počet najetých kilometrů,
informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota --
True pokud je volné a False pokud je vypůjčené).
Vytvoř funkci __init__ pro třídu Auto. Registrační značku, značku a typ vozidla a
počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu.
Poslední atribut nastav jako False, tj. na začátku je vozidlo volné.

Vytvoř objekty, které reprezentují všechny automobily půjčovny.
"""

class Auto:
  def __init__(self, spz, car, km, free = True):
    self.spz =spz
    self.car = car
    self.km = km
    self.free = free
  def evidence(self):
    if self.free:
      return f"Vozidlo {self.car} s poznavaci znackou {self.spz} a {self.km} najetymi kilometry je volne."
    else:
      return f"Vozidlo {self.car} s poznavaci znackou {self.spz} a {self.km} najetymi kilometry neni volne."


peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, False)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

print(peugeot.evidence())
print(skoda.evidence())