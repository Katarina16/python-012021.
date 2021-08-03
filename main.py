# koment ctrl + /
# item = {"title": "Čajová konvička s hrnčekom","price": "899", "inStock": "True"}
#
# item["price"] = 929
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

sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}

sausages["Adam"] = 0 #uprabí hodnotu pre Adama
sausages.pop("Adam")  #odoberie Adama zo slovníka
print(len(sausages))


