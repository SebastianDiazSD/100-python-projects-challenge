# 🎨 Color Palette Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-blue?logo=numpy)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green) ![Portfolio
Project](https://img.shields.io/badge/Portfolio-Project-informational)

A web application that extracts the **top 10 dominant colors from any
uploaded image** and presents them as a clean visual palette with HEX
codes.

Inspired by minimalist palette tools such as **Flat UI Colors**, this
project focuses on combining **data processing, machine learning, and
web development** to transform raw images into usable color palettes for
design and development workflows.

Developed as part of the **100 Python Projects Challenge** and built
with the goal of showcasing practical Python engineering and creative
problem‑solving.

🇨🇴 Built with precision, creativity, and a touch of Colombian
engineering spirit.

------------------------------------------------------------------------

# Preview

Upload an image and instantly generate a palette showing the most
representative colors detected in the image.

Typical output:

    #2ecc71
    #3498db
    #9b59b6
    #e74c3c
    #f1c40f
    ...

Each color is displayed visually alongside its **HEX code**, making it
easy to reuse in:

-   CSS
-   UI design systems
-   Branding palettes
-   Graphic design tools

------------------------------------------------------------------------

# Features

• Upload any image\
• Automatic extraction of dominant colors\
• HEX code generation for each color\
• Clean palette visualization\
• Fast image processing using optimized numerical computation

------------------------------------------------------------------------

# Technology Stack

  Technology     Purpose
  -------------- ----------------------------------------
  Python         Core programming language
  Flask          Web application framework
  NumPy          Efficient numerical operations
  Pillow         Image processing
  scikit‑learn   KMeans clustering for color extraction
  HTML / CSS     Frontend interface

------------------------------------------------------------------------

# How It Works

1.  The uploaded image is resized to improve processing speed.
2.  Pixel data is converted into a NumPy array.
3.  **KMeans clustering** groups similar colors together.
4.  The cluster centers represent the **dominant colors** in the image.
5.  Colors are converted from **RGB to HEX** and displayed as a palette.

This approach produces cleaner palettes than simple frequency counting
because visually similar shades are grouped into representative colors.

------------------------------------------------------------------------

# Installation

Clone the repository:

``` bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
```

Navigate to the project folder:

``` bash
cd 92-color-palette-generator
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run the application:

``` bash
python app.py
```

Open in your browser:

    http://127.0.0.1:5000

------------------------------------------------------------------------

# Project Structure

    92-color-palette-generator
    │
    ├── app.py
    ├── requirements.txt
    ├── templates
    │   └── index.html
    ├── static
    │   └── uploads
    └── README.md

------------------------------------------------------------------------

# Use Cases

This tool is useful for:

-   UI/UX designers extracting palettes from inspiration images
-   Frontend developers generating CSS color schemes
-   Branding teams analyzing visual identity colors
-   Data visualization styling
-   Creative coding projects

------------------------------------------------------------------------

# Repository Context

This project is **Project 92** in the *100 Python Projects Challenge*, a
collection of practical Python applications designed to demonstrate
real-world engineering skills and creative software development.

------------------------------------------------------------------------

# License

MIT License
