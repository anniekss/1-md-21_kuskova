import json
def add_product_to_json():
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"products": []}

    name = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    weight = input("Введите вес продукта: ")

    new_product = {
        "name": name,
        "price": price,
        "weight": weight
    }

    data["products"].append(new_product)

    with open('products.json', 'w') as file:
        json.dump(data, file, indent=4)
def read_and_display_json():
    try:
        with open('инф1.json', 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("Файл не найден.")

add_product_to_json()
read_and_display_json()