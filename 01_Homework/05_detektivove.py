"""
Vraťme se k software pro našeho nakladatele. Nakladatel má nyní v software dva slovníky,
které obsahují informace o prodejích knih v letech 2019 a 2020.

Uvažuj, že uživatel se zajímá o prodeje konkrétní knihy. Zeptej se uživatele na název knihy
a poté vypiš informaci o tom, kolik se této knihy celkem prodalo. Nezapomeň na to,
že některé knihy byly prodávány pouze v jednom roce.
"""

prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}

kniha = input("Zadejte nazev knihy: ")
if kniha in prodeje2019 and prodeje2020:
  soucet = prodeje2019[kniha] + prodeje2020[kniha]
  print(soucet)
elif kniha in prodeje2019:
  soucet = prodeje2019[kniha]
  print(soucet)
elif kniha in prodeje2020:
  soucet = prodeje2020[kniha]
  print(soucet)
else:
  print("Tuto knihu neprodavame.")