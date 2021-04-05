"""
Uvažuj následující třídu Kontakt, která slouží k evidenci všech kontaktů (např. zákazníků,
zaměstnanců, uchazečů o práci atd.).

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

Vytvoř třídu Uchazec, která bude dědit od třídy Kontakt a která reprezentuje uchazeče o práci.
Uchazeč o práci bude mít navíc atribut datum_pohovoru a zapis_z_pohovoru. Datum pohovoru objekt
získá z parametru a zápis z pohovoru je na začátku prázdný řetězec "".

Dále přidej funkci uloz_zapis(), která bude mít jako parametr textový zápis pohovoru.
Tato funkce ohlídá, zda uživatel omylem nezadává zápis k pohovoru, který ještě neproběhl.
Na začátku funkce porovnej aktuální datum a datum pohovoru. Pokud podle data pohovor ještě neproběhl,
vrať chybový text, který informuje uživatele o chybě. Pokud již podle data pohovor proběhl, ulož zápis
a vrať text s informací, že zápis byl uložen.
"""
from datetime import datetime
class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email
  def getInfo(self):
    return f"Uchazec {self.jmeno}:"

class Uchazec(Kontakt):
  def __init__(self, jmeno, email, datum_pohovoru):
    super().__init__(jmeno, email)
    self.datum_pohovoru = datum_pohovoru
    #datum_pohovoru = datetime.strftime(datum_pohovoru, "%d. %m. %Y, %H:%M")

  def uloz_zapis(self, zapis_z_pohovoru=""):
    self.zapis_z_pohovoru = zapis_z_pohovoru
    if self.datum_pohovoru > datetime.now():
      return f"Pohovor jeste neprobehl."
    else:
      return f"Pohovor ze dne {self.datum_pohovoru} s uchazecem {self.jmeno} probehl uspesne a zde je jeho zapis: {self.zapis_z_pohovoru}"

datum_pohovoru = input("Zadejte datum pohovoru: ")
datum_pohovoru = datetime.strptime(datum_pohovoru, "%d.%m.%Y")
poh = Uchazec("Karel", "karel@gmail.com", datum_pohovoru)

print(poh.uloz_zapis("Uchazec do tymu osobnostne zapadne."))