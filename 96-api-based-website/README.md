# 🌐 API-Based Website --- Dictionary Service

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?logo=flask)
![REST API](https://img.shields.io/badge/API-REST-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success) 

------------------------------------------------------------------------

## 🇨🇴 Overview

**API-Based Website --- Dictionary Service** is a lightweight web
application that integrates with a public REST API to retrieve word
definitions and linguistic information in real time.

The application provides a clean and intuitive interface where users can
search for English words and instantly obtain definitions, phonetics,
grammatical classification, and example usage.

The project demonstrates practical integration between a Python backend
and an external data service through HTTP requests, delivering
structured data to a web interface.

------------------------------------------------------------------------

## ✨ Features

-   🔎 Real-time word search
-   📖 Definitions retrieved from a public Dictionary API
-   🔤 Phonetic pronunciation display
-   🧠 Part of speech classification
-   📝 Example sentence when available
-   ⚡ Fast API requests and lightweight design
-   🌍 Simple and accessible web interface

------------------------------------------------------------------------

## 🧱 Technology Stack

  |Layer|               Technology|
  ---|---|
  |Backend|             Python|
  |Framework|           Flask|
  |API Communication|   Requests|
  |Frontend|            HTML + CSS|
  |Data Format|         JSON|
  |Architecture|        REST API|

------------------------------------------------------------------------

## 🔗 API Integration

This service connects to the **Free Dictionary API**, a public API
providing lexical data for English words.

API endpoint used:

    https://api.dictionaryapi.dev/api/v2/entries/en/<word>

The application sends an HTTP GET request and processes the JSON
response to extract relevant linguistic information.

------------------------------------------------------------------------

## 🖥️ Application Workflow

1.  The user enters a word in the search field.
2.  The Flask backend sends an HTTP request to the Dictionary API.
3.  The API returns structured JSON data.
4.  The backend parses the response and extracts relevant information.
5.  The results are rendered dynamically on the webpage.

------------------------------------------------------------------------

## 📂 Project Structure

    96-api-based-website/

    app.py
    requirements.txt
    README.md

    templates/
        index.html

    static/
        style.css

------------------------------------------------------------------------

## ⚙️ Installation

Clone the repository:

    git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git

Navigate to the project directory:

    cd 96-api-based-website

Install dependencies:

    pip install -r requirements.txt

Run the application:

    python app.py

Open your browser and visit:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 🧪 Example Use Case

Search for a word such as:

    innovation

The application returns:

-   phonetic pronunciation
-   grammatical classification
-   official definition
-   contextual example sentence

------------------------------------------------------------------------

## 🌎 Project Context

This project forms part of a larger engineering initiative focused on
building practical Python-based systems that integrate with external
services through modern web protocols.

The objective is to demonstrate efficient communication between
applications and public data services using HTTP and RESTful
architecture.

------------------------------------------------------------------------

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

If you would like to contribute:

1.  Fork the repository
2.  Create a feature branch
3.  Submit a pull request

------------------------------------------------------------------------

## 📜 License

This project is distributed under the **MIT License**.
