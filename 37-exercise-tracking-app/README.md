# 🏋️‍♂️ Exercise Tracker (Colombian Flavor Edition 🇨🇴🔥)

Welcome, parcero! This project is part of the **100 Days of Python Challenge – Project 37**, where we build an exercise tracking app using:

- **Nutritionix API** – to interpret natural-language exercise descriptions.
- **Sheety API** – to log exercises into a Google Sheet.
- A little **Colombian flow**, because learning to code should always have sabor.

This project reads your workout description (in plain English), calculates calories burned, and logs everything automatically into a spreadsheet.

---

## ✨ Features

- Enter exercises naturally: _"jogged for 20 minutes", "did 30 push ups", "swam for 1 hour"_
- Automatically calculates:
  - Exercise name
  - Duration (minutes)
  - Estimated calories burned
- Logs data to a Google Sheet using Sheety
- Clean prompts with a subtle Colombian vibe
- Environment-variable based for secure API usage

---

## 📦 Requirements

Before running this project, make sure you have:

- Python 3.10 or later
- A Nutritionix account (for APP ID and API Key)
- A Sheety account (for your spreadsheet endpoint)
- A `.env` file or system environment variables with the following keys:

```
ENV_NIX_APP_ID=your_app_id
ENV_NIX_API_KEY=your_api_key
ENV_SHEETY_ENDPOINT=your_sheety_endpoint
ENV_SHEETY_USERNAME=your_username
ENV_SHEETY_PASSWORD=your_password
```

> ⚠️ **Do NOT commit your real API keys**. Use environment variables.

---

## 🚀 How to Run

1. Clone this repo:

```bash
git clone https://github.com/yourusername/exercise-tracker-colombian.git
cd exercise-tracker-colombian
```

2. Install dependencies:

```bash
pip install requests python-dotenv
```

3. Add your environment variables to a `.env` or system config.

4. Run the script:

```bash
python main.py
```

5. When prompted, describe your exercises:

```
Tell me which exercises you did hoy: ran 3 miles and did 25 push ups
```

6. The script will:
   - Send your text to Nutritionix
   - Calculate calories
   - Log everything into your Google Sheet
   - Respond with some friendly Colombian energy 😎🔥

---

## 📊 Example Output

```
Bienvenido parcero! Let's track your workout with some Colombian flow.
Tell me which exercises you did hoy: swam for 30 minutes

Hold on parcero… I'm checking how many calories you burned 😎🔥
✔️  Added to your workout sheet — buena esa, parcero!
Sheety says: { "status": "success" }
```

---

## 🧠 Project Structure

```
📁 project-root
│── main.py              # Main script
│── README.md            # This file
│── .env                 # Environment variables (not included)
```

---

## 🇨🇴 Colombian Touch Added

This project intentionally keeps everything in English but adds small elements of Colombian flavor to make it feel more personal, warm, and fun — because we write code, but we also enjoy the vibes.

If you want to turn up the Colombian style even more (or make it more subtle), just let me know, parcero.

---

## 🙌 Credits

Built as part of the **100 Days of Python Bootcamp**.

Customized with ❤️, Python, and that unmistakable Colombian sabor.

---

## 📝 License

This project is open-source under the MIT License. Feel free to remix, improve, and share con toda la buena energía.