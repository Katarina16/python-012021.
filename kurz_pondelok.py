# koment ctrl + /
item = {"title": "Čajová konvička s hrnčekom","price": "899", "inStock": "True"}

#item["price"] = 929
# item["weight"] = 0.5 #pridá ďalší atribút do slovníka
#
# print(item)
#
# print("Názov položky je" + item["title"] + " cena " + str(item["price"]))
#
# print('G','F','G', sep=' ')
#
# print("Cena položky je", item["price"])
#
# print(f"Cena položky je {item['price']}")  #umožni vypsat string a int
#
# if "price" in item:
#     print(item["price"])
# else:
#     print("Cena není zadaná")
#
# if "weight" in item:
#     print(f"Hmostnosť je {item['weight']} kg.")
# else:
#     print("Hmotnost není zadaná")

# sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}

# sausages["Adam"] = 0 #uprabí hodnotu pre Adama
# sausages.pop("Adam")  #odoberie Adama zo slovníka
# print(len(sausages))

# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu.
# Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis).
# Vypiš obsah slovníku pomocí funkce print().

# vysvedcenie2 = {"predmet": ["český jazyk", "matematika" ,"dejepis"], "známka": ["1","1","1"]}

# vysvedcenie = {"český jazyk": 1, "matematika": 1, "dejepis": 1}

# vysvedcenie = {"predmet": "český jazyk"}

#print(vysvedcenie)

#Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
#U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.

#sales = {
#    "Zkus mě chytit": 4165,
#    "Vrah zavolá v deset": 5681,
#    "Zločinný steh": 2565,
#}

#sales["Noc, která mě zabila"] = 0
#sales["Vrah zavolá v deset"] = 5781
#print(sales)

#Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int!
#Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je,
#vypiš uživateli, co vyhrál.
#Odeber výhru pro daný lístek ze slovníku, abychom tam evidovali pouze nevydané ceny.

# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }
#
#
# cislo = int(input("Zadaj číslo: "))
#
# if cislo in tombola:
#     print(tombola[cislo])
#     tombola.pop(cislo)
#     print(tombola)
# else:
#     print("Ćíslo nebolo víťazné")

#Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl,
#že každý z hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program,
#který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost.
#Hostu na seznamu, který zadá správné heslo, vypíše program text: “Smíš vstoupit.”

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

meno = input("Meno: ")


if meno in passwords:
    heslo = input("Heslo: ")
    if heslo in passwords[meno]:
        print("Smíš vstoupit")
    else:
        print("Heslo nesprávne")
else:
   print("Meno nie je na zozname")

# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu.
# Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis).
# Vypiš obsah slovníku pomocí funkce print().

# vysvedcenie2 = {"predmet": ["český jazyk", "matematika" ,"dejepis"], "známka": ["1","1","1"]}

# vysvedcenie = {"český jazyk": 1, "matematika": 1, "dejepis": 1}

# vysvedcenie = {"predmet": "český jazyk"}

#print(vysvedcenie)

#Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
#U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.

#sales = {
#    "Zkus mě chytit": 4165,
#    "Vrah zavolá v deset": 5681,
#    "Zločinný steh": 2565,
#}

#sales["Noc, která mě zabila"] = 0
#sales["Vrah zavolá v deset"] = 5781
#print(sales)

#Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int!
#Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je,
#vypiš uživateli, co vyhrál.
#Odeber výhru pro daný lístek ze slovníku, abychom tam evidovali pouze nevydané ceny.

# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }
#
#
# cislo = int(input("Zadaj číslo: "))
#
# if cislo in tombola:
#     print(tombola[cislo])
#     tombola.pop(cislo)
#     print(tombola)
# else:
#     print("Ćíslo nebolo víťazné")

#Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl,
#že každý z hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program,
#který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost.
#Hostu na seznamu, který zadá správné heslo, vypíše program text: “Smíš vstoupit.”

# passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
#
# meno = input("Meno: ")
#
#
# if meno in passwords:
#     heslo = input("Heslo: ")
#     if heslo in passwords[meno]:
#         print("Smíš vstoupit")
#     else:
#         print("Heslo nesprávne")
# else:
#    print("Meno nie je na zozname")

# Napiš program pro operátora společnosti, který poskytuje informaci, zda byl balík předán kurýrovi.
# Nejprve se uživatele zeptej na kód balíku.
# Následně podle hodnoty ve slovníku vypiš větu Balík byl předán kurýrovi nebo Balík zatím nebyl předán kurýrovi.
# Pokud balík není ve slovníku, vypiš Balík neexistuje.

# baliky = {
#     "B541X": True,
#     "B547X": False,
#     "B251X": False,
#     "B501X": True,
#     "B947X": False,
# }
#
# kod = input("Zadaj kód balíka: ")
#
# if kod in baliky:
#     if baliky[kod] == True:
#         print(f"Balík s kodom {baliky[kod]} bol predaný kurierovi")
#     else:
#         print(f"Balík s kodom {baliky[kod]} nebol predaný kurierovi")
# else:
#    print("Balík neexistuje")

# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník.
# Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož.
# Následně naprogramuj následující varianty:
#
# Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
# Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů.
# Následně součástku odeber ze slovníku, protože je vyprodaná.
# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši,
# a sniž počet součástek na skladě o množství požadované zákazníkem.

# sklad = {
#   "1N4148": 250,
#   "BAV21": 54,
#   "KC147": 147,
#   "2N7002": 97,
#   "BC547C": 10
# }
#
# kod = input("Zadaj kód súčiastky: ")
#
# if kod in sklad:
#     mnozstvo = int(input("Zadaj mnozstvo: "))
#     if sklad[kod] >= mnozstvo:
#         sklad[kod] -= mnozstvo
#         print(f"Na sklade ostalo {sklad[kod]} kusov")
#     else:
#         print(f"Na sklade je iba {sklad[kod]} kusov")
# else:
#    print("Súčiastka nie je na sklade")

# Firma eviduje volné meetingové místnosti v průběhu dne ve slovníku.
# Klíč slovníku je hodina a hodnotou slovníku seznam zasedaček, které jsou v té době volné.\
# Napiš software, který se zeptá uživatele na číslo hodiny, kdy chce zamluvit meeting room.
# Poté vypíše počet volných místností, které jsou k dispozici. Pokud není k dispozici žádná místnost, program vypíše

# volnePokoje = {
#     9: ["Amadeus", "Goya", "Vlasy"],
#     10: ["Forman", "Goya"],
#     11: [],
#     12: ["Amadeus", "Vlasy"]
# }
#
# hodina = int(input("Zadej hodinu: "))
# print(f"Pocet volnych zasedacek je {len(volnePokoje[hodina])}")

#Ve slovníku níže vidíš Morseovu abecedu, kde jako klíč slouží znak v klasické abecedě a jako hodnota zápis znaku v Morseově abecedě.

# morseCode = {
#     "0": "-----",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
#     "a": ".-",
#     "b": "-...",
#     "c": "-.-.",
#     "d": "-..",
#     "e": ".",
#     "f": "..-.",
#     "g": "--.",
#     "h": "....",
#     "i": "..",
#     "j": ".---",
#     "k": "-.-",
#     "l": ".-..",
#     "m": "--",
#     "n": "-.",
#     "o": "---",
#     "p": ".--.",
#     "q": "--.-",
#     "r": ".-.",
#     "s": "...",
#     "t": "-",
#     "u": "..-",
#     "v": "...-",
#     "w": ".--",
#     "x": "-..-",
#     "y": "-.--",
#     "z": "--..",
#     ".": ".-.-.-",
#     ",": "--..--",
#     "?": "..--..",
#     "!": "-.-.--",
#     "-": "-....-",
#     "/": "-..-.",
#     "@": ".--.-.",
#     "(": "-.--.",
#     ")": "-.--.-"
# }
#
# vstup = input("Zadej vstup: ")
# for i in vstup:
#     print(morseCode[i], end=" ")

# Vraťme se k software pro našeho nakladatele. Nakladatel má nyní v software dva slovníky,
# které obsahují informace o prodejích knih v letech 2019 a 2020.
# Uvažuj, že uživatel se zajímá o prodeje konkrétní knihy.
# Zeptej se uživatele na název knihy a poté vypiš informaci o tom, kolik se této knihy celkem prodalo.
# Nezapomeň na to, že některé knihy byly prodávány pouze v jednom roce.

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
}

kniha = input("Zadej název knihy: ")
sucet = 0
if kniha in prodeje2019:
    sucet = sucet + prodeje2019[kniha]
sucet = sucet + prodeje2020[kniha]
print(f"Celkem sa prodalo {sucet} kusov.")


# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
#
# sucet = 0
# for nazev, prodano in sales.items():
#     sucet = sucet + prodano
#
# print(f"Bolo predané {sucet} kusov knih")


# books = [
#   {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#   {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#   {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
# ]
#
#
# sucet = 0
# for polozka in books:
#     sucet = sucet + polozka["sold"] * polozka["price"]



# Gustav je vášnivým čtenářem detektive z našeho nakladatelství a navíc si zapisuje knihy, které přečetl.
# Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.
# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

# books = [
#     {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
#     {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
#     {"title": "Past", "pages": 390, "rating": 4},
#     {"title": "Popel popelu", "pages": 411, "rating": 10},
#     {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
#     {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
#     {"title": "Zločinný steh", "pages": 542, "rating": 8},
#     {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
#     {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
# ]
#
# sucet = 0
# for pocet in books:
#     sucet = sucet + pocet["pages"]
#
# print(f"Gustan prečítal {sucet} strán")
#
# sucetKnih = 0
# for hodnotenie in books:
#     if hodnotenie["rating"] >= 8:
#         sucetKnih = sucetKnih + 1
#
# print(sucetKnih)

# Uvažujme vysvědčení, které máme zapsané jako slovník.
#
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

# schoolReport = {
#   "Český jazyk": 1,
#   "Anglický jazyk": 1,
#   "Matematika": 1,
#   "Přírodopis": 2,
#   "Dějepis": 1,
#   "Fyzika": 2,
#   "Hudební výchova": 4,
#   "Výtvarná výchova": 2,
#   "Tělesná výchova": 3,
#   "Chemie": 4,
# }
#
# sucet = 0
# pocet = 0
# for nazev, znamka in schoolReport.items():
#     sucet += znamka
#     pocet += 1
#
# print(sucet/pocet)
#
#
# for nazev2,znamka2 in schoolReport.items():
#   if znamka2 == 1:
#     print(nazev2)


# V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu.
# Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji,
# tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

p = "P"
for SPZ,majitel in plates.items():
  if p in SPZ:
    print(majitel)



