import json

# Чтение файла
with open("products.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Ввод данных от пользователя
name = input("Введите название: ")
price = int(input("Введите цену: "))
weight = int(input("Введите вес: "))
available_input = input("Есть в наличии? (да/нет): ")

available = True if available_input.lower() == "да" else False

new_product = {
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
}

data["products"].append(new_product)

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("\nОбновленный список:\n")

for product in data["products"]:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    
    print()