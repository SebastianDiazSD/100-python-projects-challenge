# 🔐 Random Password Generator 🇨🇴

¡Qué más pues! This is a **Random Password Generator** built with Python that helps you create strong, secure passwords — whether you want something organized or something fully unpredictable.

## 🧠 How It Works

You can generate two types of passwords:

### ✅ Structured Mode
- The password is made up of:
  - Random **letters** (like `a`, `Q`, `z`) → shuffled
  - Then random **numbers** (like `3`, `9`) → shuffled
  - Then random **symbols** (like `@`, `%`) → shuffled
- Characters are grouped **by type**, but **shuffled within each group**.
- It's organized but still offers a bit of randomness.
- Example: `aZb13$#@`

### 🔐 Scrambled Mode (Extra Secure)
- All characters (letters, numbers, symbols) are mixed **completely at random**.
- Maximum chaos = maximum security.
- Example: `3a%Z1b@#`

When you run the script, it will:

1. Ask **how many letters**, **numbers**, and **symbols** you want in your password.
2. Ask if you prefer:
   - ✅ **Structured Mode**: Organizes your password by type (letters → numbers → symbols), but shuffles within each group.
   - 🔐 **Scrambled Mode**: Mixes all characters together for full-on randomness.
3. Generate a password based on your inputs and print the final result.

---

## 🎛️ Example Interaction

```bash
How many letters would you like? 4
How many numbers would you like? 2
How many symbols would you like? 2
Choose password mode: structured[1] or scrambled[2]? 2

Your scrambled password is: 3a@Lq9$Z
```
---

## 🛠️ Features & Tools Used

- `for` loops to build character lists step-by-step. 🔁
- Python’s `random` module for all randomness. 🎲
- `shuffle()` to randomize characters in lists. 🔀

---

## 📜 Character Lists
```
python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
```
