# 🇨🇴 Quizzler App – Project 33/100 (Python Challenge)

Hey there! 👋 This is my **33rd project** from my *100 Days of Python Challenge*.  
It’s a fun little quiz app made with **Tkinter** and an **API connection** to the Open Trivia Database.

You can test your trivia skills, answer multiple-choice questions, and see your score go up in real time.  
When you answer correctly, the app flashes a *green border*; when you’re wrong, it flashes *red* — just like a traffic light in Bogotá 😉.

“Coding from Colombia with a cup of tinto ☕”

---

## 🎮 Features

✅ Fetches 50 random multiple-choice questions from the [Open Trivia DB API](https://opentdb.com/).  
✅ Uses **Tkinter** for the GUI (simple, clean, and fast).  
✅ Color feedback for answers (green = correct, red = incorrect).  
✅ Keeps track of your current score.  
✅ Option to quit the quiz at any time with confirmation.

---

## 🧠 How It Works

1. The app fetches 50 questions from the API.  
2. Each question has 4 answer options (randomized).  
3. When you click an answer, the border changes color:  
   - 🟩 **Green** if you got it right  
   - 🟥 **Red** if you got it wrong  
4. Your score updates, and after 1 second, the next question appears.  
5. When you finish, the quiz lets you know that you reached the end. 🎉  

---

## 🧰 Tech Stack

- 🐍 Python 3  
- 🎨 Tkinter (GUI)  
- 🌐 Requests (for API calls)  
- ❤️ Built with coffee and Colombian energy ☕  

---

## 🚀 How To Run

Make sure you have **Python 3** installed.

1. Clone this repo:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   cd 33-trivia-questions
   ```
2. Install dependencies (if needed):
   ```bash
   pip install requests
   ```
3. Run the app:
   ```bash
   python main.py
   ```

---

## 💡 Lessons Learned
- How to work with APIs in Python.
- How to manage multiple files and classes for clean structure.
- Handling Tkinter feedback and animations.
- Debugging GUI elements — patience and coffee are key ☕
