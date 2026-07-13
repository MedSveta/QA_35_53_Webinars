# list(список) ...[1, "str", True, 3.8]
# ...упорядоченный, изменяемый, может хранить дубли
# tuple (1, "ftg", False)
# dict {"e": 2}
# set {1,2,"try"}

person = {
    "name": "Sveta",
    "age": 22,
    "city": "Haifa",
}
print(person)

empty_dict = {}
print(empty_dict)
print("Count of keys: ", len(person))
print("Count of values: ", len(person.values()))

print(person["name"])
print(person["age"])
print(person["city"])

print(person.get("cita"))
print(person.get("cita", "not found"))

person["phone"] = '0123456789'
print(person)
person["age"] = 33
print(person)
del person["age"]
print(person)

print("name" in person)
print("email" not in person)

prices = {
    "apple": 100,
    "banana": 200,
    "orange": 300,
    "cherry": 400,
}
for product in prices:
    print("Product: ", product)

for product, price in prices.items():
    print(f"Product: {product}, Price: {price}")

print(list(prices.keys()))
print(list(prices.values()))
print(sum(prices.values()))

dict_any_types = {
    1: "paz",
    "two": 2,
    (0, 1): "rtfyt"}

dict_any_types[(True, False)] = True
print(dict_any_types)
dict_any_types[(False, True)] = False
print(dict_any_types)
print((True, False) == (1, 0))
dict_any_types[False] = False
print(dict_any_types)

# set()
color = {"red", "green", "blue"}
numbers_set = {1, 3, 5, 3, 2, 1, 1, 6, 3}
print(numbers_set)
empty_set = set()
print(empty_set)
print(type(empty_dict))
print(type(empty_set))

names = ["Sveta", "Masha", "Dima", "Sveta"]
print(names)
unique_names = set(names)
print(unique_names)

unique_names.add("Misha")
print(unique_names)
print(len(unique_names))
print("Sveta" in names)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # объединение {1, 2, 3, 4, 5, 6}
print(a & b)  # пересечение {3, 4}
print(a - b)  # разность {1, 2}
print(b - a)

english = {"Anna", "Vova", "Misha"}
russian = {"Misha", "Anna", "Sveta"}
print(english & russian)
print(english | russian)

phone_book = {"Sveta": "053-333-3333",
              "Masha": "053-444-3333"}
name = "Misha"
if name in phone_book:
    print(f"Phone {name}: {phone_book[name]}")
else:
    print(f"Number of {name} is not in phone book ")


# Создайте словарь с тремя товарами и их ценами.
#   а) выведите цену одного товара по ключу;
#   б) добавьте новый товар;
#   в) выведите сумму всех цен через sum(...values()).

products = {"milk": 2, "bread": 3, "meat": 4}
print(products["milk"])
products["salt"] = 5
print(products)
print(sum(products.values()))

wild =["tiger", "camel", "cat", "lion", "puma"]
pet = ["cat", "dog", "mouse", "lion"]
print(set(wild) & set(pet))