# product.py

products = {
    1: {"name": "Rice", "price": 60, "quantity": 10},
    2: {"name": "Wheat Flour", "price": 50, "quantity": 15},
    3: {"name": "Sugar", "price": 45, "quantity": 20},
    4: {"name": "Milk", "price": 30, "quantity": 25},
    5: {"name": "Bread", "price": 40, "quantity": 12},
    6: {"name": "Cooking Oil", "price": 120, "quantity": 10},
    7: {"name": "Salt", "price": 25, "quantity": 30},
    8: {"name": "Tea", "price": 150, "quantity": 8},
}


def display_products():
    print("\n========== AVAILABLE PRODUCTS ==========")
    print("ID\tProduct\t\tPrice\tStock")
    print("----------------------------------------")

    for product_id, product in products.items():
        print(
            f"{product_id}\t{product['name']:<15}"
            f"₹{product['price']}\t{product['quantity']}"
        )


def search_product(name):
    for product in products.values():
        if product["name"].lower() == name.lower():
            return product

    return None


def check_stock(product_id, quantity):
    if product_id in products:
        return products[product_id]["quantity"] >= quantity

    return False


def reduce_stock(product_id, quantity):
    if check_stock(product_id, quantity):
        products[product_id]["quantity"] -= quantity
        return True

    return False