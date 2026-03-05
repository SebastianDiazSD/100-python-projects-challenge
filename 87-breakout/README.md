# Project 87 --- Breakout 🇨🇴
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-87-orange)
![Challenge](https://img.shields.io/badge/Challenge-100%20Python%20Projects-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Progress](https://img.shields.io/badge/Progress-87%2F100%20Projects-blue)

Part of my **100 Python Projects Challenge**.

This project recreates the classic **Breakout arcade game**, originally
developed in the 1970s by Steve Wozniak before he co‑founded Apple. The
objective is simple: control a paddle to bounce a ball and destroy a
wall of bricks.

This version adds a small **Colombian touch** while focusing on clean
Python structure and object‑oriented programming.

------------------------------------------------------------------------

# Gameplay

The player controls a paddle at the bottom of the screen and must
prevent the ball from falling. Each time the ball hits a brick, the
brick disappears and the score increases.

To make the game progressively more challenging:

-   Each time the ball hits the paddle, the **speed slightly increases**
-   The speed increase has a **maximum limit** to keep the game playable

------------------------------------------------------------------------

# Features

• Paddle controlled with keyboard\
• Ball physics and collision detection\
• Brick destruction system\
• Score tracking\
• Progressive difficulty\
• Object-oriented project structure

------------------------------------------------------------------------

# Colombian Touch 🇨🇴

The brick colors are inspired by fruits commonly found in Colombia:

Yellow → Pineapple 🍍\
Orange → Mango 🥭\
Red → Watermelon 🍉\
Green → Lulo

The scoreboard references **Bogotá** as a small tribute.

------------------------------------------------------------------------

# Project Structure
```bash
87_breakout/

main.py --- main game loop\
paddle.py --- paddle class\
ball.py --- ball physics and speed control\
brick.py --- brick objects\
scoreboard.py --- score display
```
------------------------------------------------------------------------

# Controls

Left Arrow → Move paddle left\
Right Arrow → Move paddle right

------------------------------------------------------------------------

# Requirements

Python 3.x

This project uses the built‑in **turtle graphics module**, so no
additional packages are required.

------------------------------------------------------------------------

# How to Run

Clone the repository:
```bash
git clone
https://github.com/SebastianDiazSD/100-python-projects-challenge.git
```
Navigate to the project folder:
```bash
cd 87_breakout
```
Run the game:
```bash
python main.py
```
------------------------------------------------------------------------

# Learning Goals

This project focuses on:

• Object-oriented design\
• Game loop architecture\
• Collision detection\
• Progressive difficulty mechanics\
• Clean code organization for larger Python projects
