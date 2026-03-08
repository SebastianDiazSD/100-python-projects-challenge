# ☕ Cafe & Wifi REST API

A RESTful API built with Flask and SQLAlchemy that allows users to discover, add, update, and manage remote-work-friendly cafes.

This project demonstrates how to build a complete RESTful API from scratch — including database modeling, serialization, CRUD operations, HTTP status codes, and API documentation publishing with Postman.

Perfect for developers building:

* Remote work apps
* Digital nomad platforms
* Cafe discovery tools
* Productivity apps

---

## 🌍 What is REST?

REST stands for **Representational State Transfer.**

It is an architectural style for designing web APIs based on:

* Client–Server architecture
* HTTP request methods (GET, POST, PATCH, DELETE)
* Structured routes (endpoints)
* Proper HTTP status codes
* JSON responses

Instead of returning HTML pages, this API returns structured JSON data that other applications (web apps, mobile apps, or other backends) can consume.

---

# 🚀 Features

* Get a random cafe
* Retrieve all cafes
* Search cafes by location
* Add new cafes
* Update coffee prices
* Securely delete cafes with API key protection
* Fully RESTful design
* JSON responses
* Proper HTTP status codes

---

## 🛠 Tech Stack

* Python
* Flask
* SQLAlchemy
* SQLite
* Postman (for testing & documentation)

---

## 📍 API Endpoints

### 🔎GET `/random`

Returns a random cafe.

Example Response:
```json
{
  "cafe": {
    "id": 5,
    "name": "Cafe Central",
    "location": "London",
    "coffee_price": "£3.50",
    ...
  }
}
```
Returns:

* 200 OK if successful
* 404 Not Found if database is empty

---

### 📋GET `/all`

Returns all cafes in the database.

Example Response:
```json
{
  "count": 10,
  "cafes": [
    {...},
    {...}
  ]
}
```
Returns:

* 200 OK

---

### 🔍GET `/search?loc=LocationName`

Search cafes by location.

Example:
```bash
/search?loc=London
```

Returns:

* 200 OK if cafes are found
* 404 Not Found if no cafes exist in that location
* 400 Bad Request if no location parameter is provided

---

### ➕POST `/add`

Adds a new cafe.

Required Form Fields (x-www-form-urlencoded):

* name
* map_url
* img_url
* loc
* wifi
* sockets
* toilet
* calls
* seats
* coffee_price

Returns:

* 201 Created if successful
* 500 Internal Server Error if something fails

---

### 🔄PATCH `/update-price/<cafe_id>?new_price=£5.50`

Updates the coffee price for a specific cafe.

Example:

```bash
/update-price/5?new_price=£4.20
```

Returns:

* 200 OK if updated successfully
* 404 Not Found if cafe ID does not exist
* 400 Bad Request if no new_price is provided

---

### DELETE `/report-closed/<cafe_id>?api-key=TopSecretAPIKey`

Deletes a cafe (requires API key).

Example:

```bash
/report-closed/5?api-key=TopSecretAPIKey
```
Returns:

* 200 OK if deleted successfully
* 403 Forbidden if API key is invalid
* 404 Not Found if cafe does not exist

---

## 🔄 PATCH vs PUT (Important REST Concept)

In REST APIs, both PATCH and PUT are used for updating data — but they behave differently.

### PUT → Replace Everything

PUT replaces the entire resource.

If updating a cafe using PUT, you would need to send the entire cafe object again — even fields that are not changing.

It’s like replacing an entire bicycle just because the wheel broke.

### PATCH → Update Only What’s Needed

PATCH updates only specific fields.

In this API, we use PATCH to update only the coffee_price field without touching the rest of the cafe’s data.

It’s like replacing only the broken wheel instead of the whole bike.

PATCH is:

* More efficient
* Cleaner
* Better for partial updates

---

## 🔐 Security

Delete requests require an API key:
```nginx
TopSecretAPIKey
```

Returns:

* 403 if API key is invalid
* 404 if cafe does not exist

---

## 📚 Documentation

This API was tested and documented using Postman.

The full interactive documentation is available here:

[Cafe & WiFi](https://documenter.getpostman.com/view/52409019/2sBXcBoNYB)

---

## 💡 Learning Objectives

This project demonstrates:

* RESTful API architecture
* HTTP methods and status codes
* Serialization with Flask
* Database CRUD operations
* API key protection
* Professional API documentation publishing

## 🚀 Final Advice for Publishing

When publishing on Postman:

* Add descriptions to each endpoint
* Add example requests
* Add example responses
* Add status code explanations
* Add a clean collection description

That makes your API look very professional.
