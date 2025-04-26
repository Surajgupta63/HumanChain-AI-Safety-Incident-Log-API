# HumanChain AI Safety Incident Log

A Flask web application to log and manage AI safety incidents.  
Includes user authentication, incident reporting, updating, deleting, and dashboard viewing.

---

## 🛠 Tech Stack

- **Language**: Python
- **Framework**: Flask
- **Database**: SQLite (with SQLAlchemy ORM)
- **Frontend**: HTML (Jinja2 templating)

---

## ✨ Features

- User Signup, Login, Logout
- Password hashing for secure authentication
- Create, Update, Delete, and Search Incidents
- View all Incidents in a Dashboard
- Incident severity levels: `LOW`, `MEDIUM`, `HIGH`

---

## 📦 Project Structure

```
humanchain-incident-log/
├── app.py
├── db.py
├── models/
│   └── incidents.py
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── incident.html
│   └── update.html
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/humanchain-incident-log.git
cd humanchain-incident-log
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

No manual setup needed.  
The SQLite database `humanchain_incidents.db` will be automatically created when you first run the app.

### 5. (Optional) Environment Variables Setup

You can create a `.env` file (optional):

```env
SECRET_KEY=SPARKLEHOOD
DATABASE_URL=sqlite:///humanchain_incidents.db
```

*(You need to modify `app.py` slightly to load `.env` if you use this.)*

---

## 🏃 Running the Application

```bash
python app.py
```

Then open your browser at:

```
http://localhost:8000
```

---

## 📜 Available Routes

| Route            | Methods     | Description                         |
|------------------|--------------|-------------------------------------|
| `/`              | GET          | Home/Login page                     |
| `/login`         | GET, POST    | User login                          |
| `/signup`        | GET, POST    | User registration                   |
| `/logout`        | GET          | Logout the current user             |
| `/dashboard`     | GET          | View all incidents dashboard        |
| `/incident`      | GET, POST    | Create a new incident report        |
| `/update/<id>`   | GET, POST    | Update an existing incident         |
| `/delete/<id>`   | GET          | Delete an incident                  |
| `/search`        | GET, POST    | Search for an incident by ID        |

---

## ⚡ Important Notes

- Incident severity must be either `LOW`, `MEDIUM`, or `HIGH`.
- Passwords are securely handled and stored.
- Basic validation and error handling included.
- Designed for local development and demonstration purposes.

---

## 🔥 Future Enhancements (Optional)

- Admin roles and permissions
- RESTful API endpoints
- Frontend improvements (Bootstrap/React)
- Docker containerization
- Deployment to Heroku/AWS

---

## 📋 Example `requirements.txt`

```
Flask
Flask-SQLAlchemy
Werkzeug
python-dotenv
```

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🧡 Thank you for using HumanChain AI Safety Incident Log!

