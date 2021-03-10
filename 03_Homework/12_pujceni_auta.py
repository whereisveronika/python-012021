"""
Pokračuj ve své práci pro autopůjčovnu, kterou jsi začala v příkladu 11.

Třídě Auto přidej funkci pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr.
Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, vrátí text "Potvrzuji zapůjčení
vozidla" a změní hodnotu atributu, který určuje, zda je vozidlo půjčené. Pokud je vozidlo již půjčené,
vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka
a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit.
Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci
o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto.

Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat,
že funkce nedovolí půjčit stejné auto dvakrát.
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
  def get_info(self):
    return f"Vozidlo {self.car} s poznavaci znackou {self.spz} ma najeto {self.km} kilometru."


pujceni = input("Jakou znacku vozidla si chcete vypujcit? ")
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, False)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

if pujceni == "peugeot":
  print(peugeot.get_info())
  print(peugeot.pujc_auto())
elif pujceni == "skoda":
  print(skoda.get_info())
  print(skoda.pujc_auto())
else:
  print(f"Auta znacky {pujceni} nepujcujeme.")

#print(skoda.pujc_auto())
#print(skoda.pujc_auto())
