"""
Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a příkladu 12.

Přidej třídě Auto funkci vrat_auto(), která bude mít (krom obligátního self)
2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník
auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem
auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta.
Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return.

Na konec programu (mimo třídu) přidej dotaz na uživatele, kolik kilometrů zákazník ujel a
jak dlouo ho měl půjčené. Poté vypiš informaci o ceně.
"""

class Auto:
  def __init__(self, spz, car, km, free = True):
    self.spz =spz
    self.car = car
    self.km = km
    self.free = free

  def pujc_auto(self):
    if self.free:
      self.free = False
      return f"Potvrzuji zapujceni vozidla."
    else:
      return f"Vozidlo neni k dispozici."
  def vrat_auto(self, najeto, days):
    self.najeto = najeto
    self.days = days
    if self.days >= 7:
      self.cost = 300 * self.days
    else:
      self.cost = 400 * self.days
    self.free = True
    return f"Ujeli jste {self.najeto} km a cena za vypujceni vozidla je {self.cost} Kc."
  def get_info(self):
    return f"Vozidlo {self.car} s poznavaci znackou {self.spz} ma najeto {self.km} kilometru."

#pujceni = input("Jakou znacku vozidla si chcete vypujcit? ")

days = input("Kolik dni jste meli auto pujcene? ")
days = int(days)
najeto = input("Kolik jste najeli: ")
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, False)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)


print(skoda.vrat_auto(najeto, days))
#print(skoda.pujc_auto())
