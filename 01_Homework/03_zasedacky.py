"""
Firma eviduje volné meetingové místnosti v průběhu dne ve slovníku.
Klíč slovníku je hodina a hodnotou slovníku seznam zasedaček, které jsou v té době volné.
Napiš software, který se zeptá uživatele na číslo hodiny, kdy chce zamluvit meeting room.
Poté vypíše počet volných místností, které jsou k dispozici.
"""

volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

hodina = int(input("V kolik potřebujete zasedačku? "))
if hodina in volnePokoje:
  print(f"V {hodina} hodin máme volné {len(volnePokoje[hodina])} zasedačky.")
else:
  print("Zasedačky jsou přístupné pouze od 9 do 12 hodin.")