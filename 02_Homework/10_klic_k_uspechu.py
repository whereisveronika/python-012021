"""
Obchodníci v naší softwarové firmě používají jednoduchý systém, aby odhadli šanci na
úspěch potenciální zakázky. Každé zakázce přiřadí body od 0 do 10 a platí:

Pokud má zakázka méně než 5 bodů, šance na záskání je malá.
Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
Pokud má zakázka více bodů, šance na získání je vysoká.
Body přidělují podle následujících kritérií:

Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu.
Pokud potenciální zákazník podniká v automotive, přičti 3 body, pokud v retailu, přičti 2 bod, jinak 0.
Obrat: Firma nejlépe prodává zákazníkům se středním obratem. U malých většinou neuspěje,
u velkých občas ano. Pokud má firma obrat menší než 10 mil. Euro, přičti 0. Pokud je mezi
10 a 1 000 mil. Euro, přičti 3 body, jinak 1 bod.
Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body), o něco méně
v Německu a ve Francii (1 bod). Ostatním zemím dej 0.
Konference: Firma loni pořádala odbornou konferenci pro zákazníky. Pokud se zákazník konference
účastnil, přičti 1 bod, jinak 0.
Newsletter: Firma též rozesílá newsletter o svém produktu. Pokud zákazník newsletter odebírá, přičti 1 bod.
Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria.
Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False. Funkce vrátí šanci
na získání zakázky jako řetězec.
"""


def order(area, turnOver, country, conference = False, newsletter = False):
  points = 0

  if area == "Automotive" or area == "automotive":
    points += 3
  elif area == "Retail" or area == "retail":
    points += 2
  else:
    points += 0

  if turnOver < 10:
    points += 0
  elif turnOver < 1000:
    points += 3
  else:
    points += 1

  if country == "Czechia" or country == "Slovakia":
    points += 2
  elif country == "Germany" or country == "France":
    points += 1
  else:
    points += 0

  if conference == "Yes" or conference == "yes":
    points += 1
  else:
    points += 0

  if newsletter == "Yes" or conference == "yes":
    points += 1
  else:
    points += 0

  return points


area = input("Enter the area of business: ")
turnOver = input("Enter the turnover in millions: ")
turnOver = int(turnOver)
country = input("Enter the country of the business: ")
conference = input("The conference status (Yes/No): ")
newsletter = input("Signed up for a newsletter (Yes/No): ")

if order(area, turnOver, country, conference = False, newsletter = False) <= 5:
  chance = "small"
elif order(area, turnOver, country, conference = False, newsletter = False) <=8:
  chance = "average"
else:
  chance = "high"

print(f"The order gets {order(area, turnOver, country, conference, newsletter)} points so the chance of winning is {chance}.")