# 🦖 94 - Chrome Dinosaur Automation Bot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Automation](https://img.shields.io/badge/Automation-PyAutoGUI-green)
![Computer
Vision](https://img.shields.io/badge/Screen%20Detection-Pillow-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Automation project inspired by the well‑known Chrome offline dinosaur
game.\
This implementation detects obstacles directly from screen pixels and
triggers jumps automatically, allowing the game to run autonomously.

Developed as part of the **100 Python Projects Challenge** and designed
to demonstrate practical automation techniques using Python.

------------------------------------------------------------------------

# 🇨🇴 About the Project

The Chrome T‑Rex game appears when internet connectivity is unavailable.
Hidden behind this simple interface is a fast‑paced endless runner where
the dinosaur must jump over obstacles to survive.

This project automates gameplay using **screen analysis and keyboard
control**. The script continuously scans a small region in front of the
dinosaur, detects obstacles through pixel intensity changes, and
executes jump actions in real time.

Built with the same determination and resilience that characterize
Colombian innovation---focused, efficient, and designed to get the job
done.

------------------------------------------------------------------------

# ⚙️ Core Features

-   Real‑time **screen capture and pixel analysis**
-   Automated **jump execution using keyboard control**
-   Lightweight implementation with minimal dependencies
-   Adjustable detection region for different screen resolutions
-   Designed for reliable and consistent gameplay automation

------------------------------------------------------------------------

# 🧰 Technologies

  Technology   Purpose
  ------------ ----------------------------------------
  Python       Core programming language
  PyAutoGUI    Keyboard automation and screen capture
  Pillow       Image processing and pixel detection

------------------------------------------------------------------------

# 📦 Installation

Clone the repository:

``` bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 94-dinosaur-game
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# ▶️ Running the Bot

1.  Open the Chrome Dino game:

```{=html}
<!-- -->
```
    https://elgoog.im/t-rex/

2.  Ensure the dinosaur is visible on screen.

3.  Run the script:

``` bash
python main.py
```

The automation will begin after a short initialization delay.

------------------------------------------------------------------------

# 🧠 How It Works

1.  The program captures a **specific region of the screen** located
    ahead of the dinosaur.
2.  The captured image is converted into grayscale.
3.  Pixel values are scanned for **dark obstacle patterns**.
4.  When detected, the script triggers a **spacebar press** to jump.

This loop runs continuously to maintain real‑time reactions.

------------------------------------------------------------------------

# 📂 Project Structure

    94-dinosaur-game
    │
    ├── main.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# 🌎 Portfolio Context

This project forms part of the **100 Python Projects Challenge**, a
portfolio initiative showcasing practical implementations across
automation, data processing, APIs, and software development.

------------------------------------------------------------------------

# 🤝 Connect

**Sebastian Diaz**\
Technology Consultant \| Automation Enthusiast \| Builder

Committed to building practical solutions, scalable tools, and impactful
digital systems.

------------------------------------------------------------------------

# 📄 License

This project is distributed under the **MIT License**.
