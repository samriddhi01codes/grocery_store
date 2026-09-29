# cart.py

cart = []


def add_to_cart(product, quantity):
    item = {
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    }

    cart.append(item)
    print(f"{quantity} x {product['name']} added to cart.")


def remove_from_cart(name):
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print(f"{name} removed from cart.")
            return

    print("Product not found in cart.")


def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")

    total = 0

    for item in cart:
        amount = item["price"] * item["quantity"]
        total += amount

        print(
            f"{item['name']} - "
            f"₹{item['price']} x {item['quantity']} = ₹{amount}"
        )

    print("-------------------------------")
    print(f"Total: ₹{total}")


def get_total():
    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    return total