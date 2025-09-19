# ☕ Coffee Machine – Colombian Edition 🇨🇴

¡Hola! Welcome to my **Coffee Machine Project**, inspired by my love for coding and Colombian coffee.

This is a simple terminal-based Python app where users can order a coffee — espresso, latte, or cappuccino — and the machine checks if it has the resources to prepare it. Users insert coins, and the machine handles everything: verifying resources, processing the payment, giving change, and of course, making the drink.  

It’s like running a tiny coffee shop… from your terminal.

---

## 🚀 Features

- Choose from 3 drinks: **Espresso**, **Latte**, or **Cappuccino**
- Simulates inserting coins (quarters, dimes, nickels, and pennies)
- Calculates if the payment is enough and gives change
- Checks if ingredients are available before making the drink
- Tracks total **profit**
- Special commands:  
  - `'report'` → shows current machine status  
  - `'off'` → turns off the machine  
  - `'no'` → exit the game gracefully

---

## 💡 Why I Built This

I'm learning Python and wanted to create something fun but still useful to understand:
- Functions & loops
- Working with dictionaries
- User input and conditionals
- Keeping track of resources (kind of like inventory management)
- Writing clean and reusable code

Also, I just love coffee — especially the kind we have here in Colombia. ☕🇨🇴

This project helped me think more logically and write cleaner code while having fun along the way.

---

## 🧾 How to Use It

1. Clone the repo:
```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 15-coffee-machine
```
2. Run the program:
```bash
python coffee_machine.py
```

## ☕ Sample Output

```bash
What would you like today? We've got: Espresso, Latte, or Cappuccino ☕

(Type 'report' to see machine status, 'off' to shut down, or 'no' to exit)
→ latte

Please insert coins 💰
How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0

Here is your change: $0.0
Here is your latte ☕ Enjoy it, parcero!
```
