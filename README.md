# Flask Notes API

A simple REST API built with **Flask** to practice backend development concepts like:

* GET requests
* POST requests
* URL parameters
* DELETE requests
* API testing with Postman

This project was built as part of my backend learning journey.

---

## Features

* Add a new note
* View all notes
* View a single note
* Delete a note
* REST API structure

---

## Tech Stack

* Python
* Flask
* Postman (for API testing)

---

## Project Structure

```
flask-notes-api/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Add Note

POST `/add-note`

Body (form-data):

```
text : learn flask api
```

---

### Get All Notes

GET `/notes`

Example response:

```
[
  {
    "id": 1,
    "text": "learn flask"
  }
]
```

---

### Get Single Note

GET `/note/<id>`

Example:

```
/note/1
```

---

### Delete Note

DELETE `/delete-note/<id>`

Example:

```
/delete-note/1
```

---

## Run Locally

Clone the repository:

```
git clone https://github.com/yourusername/flask-notes-api.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## Learning Purpose

This project was built to practice backend fundamentals using Flask, including REST APIs and request handling.

More improvements will be added later such as:

* database integration
* authentication
* security improvements
