store_items = [
    ("Rice", 60),
    ("Wheat Flour", 45),
    ("Sugar", 42),
    ("Milk", 28),
    ("Bread", 35),
    ("Eggs", 7),
    ("Tea", 120),
    ("Biscuits", 20),
    ("Apple", 150),
    ("Banana", 50),
]


cart = {}


def display_store_items():
    
    print("")
    print("=" * 35)
    print("        AVAILABLE ITEMS")
    print("=" * 35)
    number = 1
    for name, price in store_items:          
        print(str(number) + ". " + name + " - Rs. " + str(price))
        number = number + 1
    print("=" * 35)


def get_price(item_name):
    
    price_found = 0
    for name, price in store_items:
        if name == item_name:
            price_found = price
    return price_found


def add_item():
    
    display_store_items()
    choice = int(input("Enter item number to add: "))

    if choice < 1 or choice > len(store_items):
        print("Invalid item number!")
    else:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
        else:
            item_name = store_items[choice - 1][0]
            if item_name in cart:
                cart[item_name] = cart[item_name] + quantity
            else:
                cart[item_name] = quantity
            print(str(quantity) + " x " + item_name + " added to cart.")


def view_cart():
    
    if len(cart) == 0:
        print("\nYour cart is empty.")
    else:
        print("")
        print("=" * 35)
        print("          YOUR CART")
        print("=" * 35)
        number = 1
        for name, price in store_items:
            if name in cart:
                print(str(number) + ". " + name + " | Qty: " + str(cart[name]))
            number = number + 1
        print("=" * 35)


def remove_item():
    
    if len(cart) == 0:
        print("Your cart is empty. Nothing to remove.")
    else:
        view_cart()
        choice = int(input("Enter item number to remove: "))

        if choice < 1 or choice > len(store_items):
            print("Invalid item number!")
        else:
            item_name = store_items[choice - 1][0]
            if item_name not in cart:
                print("That item is not in your cart.")
            else:
                quantity = int(input("Enter quantity to remove: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                elif quantity >= cart[item_name]:
                    del cart[item_name]
                    print(item_name + " removed from cart.")
                else:
                    cart[item_name] = cart[item_name] - quantity
                    print(str(quantity) + " x " + item_name + " removed.")


def calculate_subtotal():
    
    total = 0
    for name in cart:
        total = total + get_price(name) * cart[name]
    return total


def count_items():
    
    count = 0
    for name in cart:
        count = count + cart[name]
    return count          


def display_bill():
    
    if len(cart) == 0:
        print("\nYour cart is empty. Add some items first.")
    else:
        subtotal = calculate_subtotal()
        final_amount = subtotal

        print("")
        print("=" * 40)
        print("         GROCERY STORE BILL")
        print("=" * 40)
        for name in cart:
            price = get_price(name)
            qty = cart[name]
            print(name + ": " + str(qty) + " x " + str(price) + " = " + str(price * qty))
        print("-" * 40)
        print("Total items    : " + str(count_items()))
        print("Subtotal       : Rs. " + str(subtotal))
        print("=" * 40)
        print("TOTAL PAYABLE  : Rs. " + str(round(final_amount, 2)))
        print("=" * 40)
        print("    Thank you for shopping with us!")


def main():
    print("*" * 40)
    print("  WELCOME TO THE SIMPLE GROCERY STORE")
    print("*" * 40)
    

    while True:
        print("\n---------- MENU ----------")
        print("1. View store items")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. View cart")
        print("5. Display bill")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_store_items()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            display_bill()
        elif choice == "6":
            print("Thank you for visiting! Goodbye.")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


main()