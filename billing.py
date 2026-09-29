
# billing.py

from product import get_price
from cart import cart


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

            print(
                name + ": " +
                str(qty) + " x " +
                str(price) + " = " +
                str(price * qty)
            )

        print("-" * 40)
        print("Total items    : " + str(count_items()))
        print("Subtotal       : Rs. " + str(subtotal))
        print("=" * 40)
        print("TOTAL PAYABLE  : Rs. " + str(round(final_amount, 2)))
        print("=" * 40)
        print("    Thank you for shopping with us!")
