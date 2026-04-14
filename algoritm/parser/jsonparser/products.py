import json

with open("algoritm/parser/jsonparser/products.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for product in data["products"]:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    
    print()