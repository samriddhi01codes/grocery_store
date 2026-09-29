# 🛒 Simple Grocery Store

## 📌 Project Description

**Simple Grocery Store** is a beginner-friendly Python project that simulates a basic grocery shopping system.

The program allows customers to:

* View available grocery items
* Add items to their cart
* Remove items from their cart
* View the current cart
* Calculate the total bill
* Display the final payable amount

The project uses basic Python concepts such as **lists, tuples, dictionaries, loops, conditional statements, functions, user input, and arithmetic operations**.

---

## ✨ Features

### 1. View Store Items

Displays all available grocery items along with their prices.

### 2. Add Items to Cart

The user can select an item using its item number and enter the required quantity.

### 3. Remove Items from Cart

The user can remove a specific quantity of an item from the cart.

### 4. View Cart

Displays all items currently added to the shopping cart along with their quantities.

### 5. Display Bill

Calculates and displays:

* Individual item prices
* Quantity purchased
* Total price of each item
* Total number of items
* Subtotal
* Total payable amount

### 6. Exit

Allows the user to safely exit the grocery store program.

---

## 🛍️ Available Items

| No. | Item        | Price (Rs.) |
| --: | ----------- | ----------: |
|   1 | Rice        |          60 |
|   2 | Wheat Flour |          45 |
|   3 | Sugar       |          42 |
|   4 | Milk        |          28 |
|   5 | Bread       |          35 |
|   6 | Eggs        |           7 |
|   7 | Tea         |         120 |
|   8 | Biscuits    |          20 |
|   9 | Apple       |         150 |
|  10 | Banana      |          50 |

---

## 🧰 Technologies Used

* **Programming Language:** Python
* **Data Structures:** List, Tuple, Dictionary
* **Concepts Used:**

  * Functions
  * Loops
  * Conditional statements
  * User input
  * Dictionary operations
  * Arithmetic calculations
  * String formatting

No external libraries are required.

---

## 📂 Project Structure

```text
Grocery-Store/
│
├── main.py
├── product.py
├── cart.py
└── README.md
```

> The current program can also run as a single Python file. The project can later be divided into separate modules such as `product.py`, `cart.py`, and `billing.py`.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2: Open the Project Folder

Open the terminal inside the project folder.

### Step 3: Run the Program

```bash
python main.py
```

---

## 🎮 Program Menu

When the program starts, the following menu is displayed:

```text
---------- MENU ----------
1. View store items
2. Add item to cart
3. Remove item from cart
4. View cart
5. Display bill
6. Exit
```

The user can enter a number from **1 to 6** to perform the desired operation.

---

## 🧮 Example

Suppose the customer purchases:

```text
Rice     → 2 × Rs. 60 = Rs. 120
Milk     → 3 × Rs. 28 = Rs. 84
Bread    → 1 × Rs. 35 = Rs. 35
```

The bill will calculate:

```text
Total items    : 6
Subtotal       : Rs. 239
TOTAL PAYABLE  : Rs. 239
```

---

## 🔄 Program Flow

```text
Start
  ↓
Display Main Menu
  ↓
Choose an Option
  ↓
┌─────────────────────────────┐
│ 1. View Store Items         │
│ 2. Add Item to Cart         │
│ 3. Remove Item from Cart    │
│ 4. View Cart                │
│ 5. Display Bill             │
│ 6. Exit                     │
└─────────────────────────────┘
  ↓
Perform Selected Operation
  ↓
Return to Main Menu
  ↓
Exit
```

---

## 📚 Functions Used

| Function                | Purpose                               |
| ----------------------- | ------------------------------------- |
| `display_store_items()` | Displays all available products       |
| `get_price()`           | Finds the price of a particular item  |
| `add_item()`            | Adds an item and quantity to the cart |
| `view_cart()`           | Displays items currently in the cart  |
| `remove_item()`         | Removes items from the cart           |
| `calculate_subtotal()`  | Calculates the total cost             |
| `count_items()`         | Counts the total quantity of items    |
| `display_bill()`        | Displays the final grocery bill       |
| `main()`                | Controls the main program and menu    |

---

## 🎯 Learning Objectives

This project helps demonstrate the practical use of:

1. Python functions
2. Lists and tuples
3. Dictionaries
4. `for` and `while` loops
5. `if-elif-else` conditions
6. User input handling
7. Basic calculations
8. Modular programming concepts
9. Menu-driven programming
10. Basic shopping-cart logic

---

## 🚀 Future Improvements

The project can be improved by adding:

* Customer login and registration
* Product search
* Product stock management
* Discounts and coupons
* GST calculation
* Different payment methods
* Digital receipt generation
* Date and time on bills
* File/database storage
* Admin panel for adding and removing products
* Product categories
* Low-stock alerts

---

## 👨‍💻 Author

**Grocery Store Management System**

A Python-based beginner project developed to demonstrate fundamental programming concepts through a practical grocery shopping application.

---

## 📄 License

This project is created for **educational purposes**.