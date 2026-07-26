item_count = 0
discount_rate = 0.10
store_name = "Black Devil"
discount_floor_price = 200
date = (26, 7, 2026)
cart_items = [1, 3, 8]

catalog = {
    "milk": {"id": 1, "name": "milk", "price": 80},
    "bread": {"id": 2, "name": "bread", "price": 140},
    "sause": {"id": 3, "name": "sause", "price": 180},
    "paneer": {"id": 4, "name": "paneer", "price": 200},
    "coffee": {"id": 5, "name": "coffee", "price": 280},
}


print(f"Welcom to the {store_name}")

print(date)

total = 0
cart = set(cart_items)


def getProductList(product_ids):
    list = []

    for i in cart:

        product = None

        for j in catalog.values():
            if j["id"] == i:
                product = j

        if not (product):
            print(f"The product with {i} id is not available")
        else:
            list.append(product)

    return list


cart_items = getProductList(cart)

counter = 1

for item in cart_items:
    total += item["price"]
    print(f"Cart item {counter}: {item["name"]} - {item["price"]}")
    counter += 1


if discount_rate > 0 and total > discount_floor_price:
    discount = total * discount_rate
    total -= discount


print(f"Your total is {round(total,2)}")
