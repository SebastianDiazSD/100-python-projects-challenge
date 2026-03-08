# 🇨🇴 Colombian Online Shop

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?logo=flask)
![Stripe](https://img.shields.io/badge/Payments-Stripe-purple?logo=stripe)
![SQLAlchemy](https://img.shields.io/badge/Database-SQLAlchemy-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success) 
------------------------------------------------------------------------

## 🌎 Overview

**Colombian Online Shop** is a lightweight eCommerce web application
built with Flask that demonstrates a complete purchase flow from product
browsing to secure online payment.

The platform displays products, allows users to manage a shopping cart,
and processes payments through **Stripe Checkout**.\
Authentication features provide account registration and login
functionality, enabling a structured and secure shopping experience.

The application illustrates the integration between a Python backend, a
relational database, and an external payment provider.

------------------------------------------------------------------------

## ✨ Core Features

-   🛍 Product catalog display
-   🛒 Session‑based shopping cart
-   🔐 User registration and authentication
-   💳 Secure checkout with **Stripe**
-   📦 Order flow simulation
-   ⚡ Lightweight and responsive interface

------------------------------------------------------------------------

## 🧱 Technology Stack

  |Layer|            Technology|
  ---|---|
  |Backend|          Python|
  |Web Framework|    Flask|
  |Database|         SQLite + SQLAlchemy|
  |Authentication|   Flask‑Login|
  |Payments|         Stripe Checkout API|
  |Frontend|         HTML + CSS|
  |Data Format|      JSON|

------------------------------------------------------------------------

## 💳 Payment Integration

Payments are handled through **Stripe Checkout**, which provides a
secure hosted payment page and manages the transaction process.

Key features of the Stripe integration include:

-   Secure card processing
-   Hosted checkout session
-   Automatic success and cancel redirects
-   Real payment support in production environments

Stripe documentation:

    https://stripe.com/docs/payments/checkout

Test card for development:

    4242 4242 4242 4242

------------------------------------------------------------------------

## 🖥️ Application Workflow

1.  A visitor browses available products on the homepage.
2.  Items are added to the shopping cart using session storage.
3.  Registered users proceed to checkout.
4.  A **Stripe Checkout session** is created dynamically.
5.  Stripe processes the payment securely.
6.  The application redirects the user to either a success or
    cancellation page.

------------------------------------------------------------------------

## 📂 Project Structure

    97-colombian-online-shop/

    app.py
    products.py
    requirements.txt
    README.md

    templates/
        base.html
        index.html
        login.html
        register.html
        cart.html
        success.html
        cancel.html

    static/
        style.css

------------------------------------------------------------------------

## ⚙️ Installation

Clone the repository:

    git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git

Navigate to the project directory:

    cd 97-colombian-online-shop

Install dependencies:

    pip install -r requirements.txt

Configure your Stripe key inside a `.env` file:

    STRIPE_SECRET_KEY=your_stripe_secret_key

Run the application:

    python app.py

Open the browser and visit:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 📦 Example Products

The store includes sample products inspired by Colombian culture:

-   Premium Colombian Coffee
-   Handmade Wayuu Mochila
-   Colombian Cacao Chocolate

These products demonstrate how catalog data can be structured and
displayed within the application.

------------------------------------------------------------------------

## 🔐 Security Considerations

For production deployment, additional improvements are recommended:

-   Password hashing
-   Environment variable management
-   HTTPS configuration
-   Database migration support
-   Payment webhook verification

------------------------------------------------------------------------

## 🤝 Contributions

Suggestions and improvements are welcome.\
Feel free to fork the repository and submit a pull request.

------------------------------------------------------------------------

## 📜 License

Distributed under the **MIT License**.

------------------------------------------------------------------------

## 🇨🇴 Engineering with Colombian persistence

Built with discipline, creativity, and the resilient spirit that defines
Colombian builders.
