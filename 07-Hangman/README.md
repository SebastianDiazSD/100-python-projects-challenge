# 🇨🇴 Hangman en Python 🎯

¡Bienvenid@!  
This is a fun little **Hangman** project made with Python — step by step, todo by todo. The idea is to go through each part and build the full game from scratch. Ideal if you're learning to code or just want to practice your logic and Python skills.

---

## 🎯 What's the Goal?

We’re going to build a **classic Hangman game**: the one where you guess letters of a hidden word before the little stick figure meets its doom (👻).  
I’ve broken it down into **10 easy-to-follow TODOs**

---

## 🔥 The Vibe

This project is perfect for beginners or anyone who wants to brush up on:

- Python basics
- Loops, conditionals, and lists
- Working with user input
- Building game logic from scratch

---

## ✅ TODO List (Let's get it done 💪)

1. **ToDo 1** – Randomly pick a word from `word_list`, assign it to `chosen_word`, and print it out to check it's working.
2. **ToDo 2** – Ask the user to guess a letter, save it in a variable called `guess`, and make it lowercase.
3. **ToDo 3** – Check if the letter (`guess`) is in `chosen_word`. If yes, print “Right”, if not, print “Wrong”.
4. **ToDo 4** – Create a blank placeholder list to show the guessed letters (like `_ _ _ _ _`).
5. **ToDo 5** – If the guess is correct, replace the blanks with the correct letters in the right spots.
6. **ToDo 6** – Use a `while` loop so the user can keep guessing until they win or lose.
7. **ToDo 7** – Track the letters that have already been guessed to avoid repeating.
8. **ToDo 8** – Create a `lives` variable (start at 6) to keep track of failed attempts.
9. **ToDo 9** – If the letter is not in the word, subtract a life. If lives hit 0, print “You lose”.
10. **ToDo 10** – Show some cool ASCII art depending on how many lives are left.

---

## 🧱 Project Structure

We'll be working with three main files:
hangman_art.py
hangman_words.py
hangman_ToDos.py

The final version of the code will be in hangman_final.py
