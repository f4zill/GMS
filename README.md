# 🏋️ Gym Management System

A full-stack Gym Management Web Application built using **Flask**, **MongoDB**, and **Bootstrap**. This app allows you to manage gym members, trainers, equipment, plans, and attendance through a sleek web interface.

---

## 📦 Features

* 🢑 CRUD operations for Members, Trainers, and Staff
* 🏋️ Equipment and Workout Plans Management
* 🗕️ Track Attendance and Schedule
* 🔍 Search and filter records
* ☁️ Hosted on Render (or can be run locally)

---

## 🚀 Tech Stack

| Frontend               | Backend        | Database              |
| ---------------------- | -------------- | --------------------- |
| HTML5, CSS3, Bootstrap | Flask (Python) | MongoDB (via PyMongo) |

---

## 🔧 Setup Instructions

### ✅ Prerequisites

* Python 3.9 to 3.10 (⚠️ Do **not** use 3.11+ due to PyMongo/SSL issues)
* MongoDB Atlas (or local MongoDB)
* Git

---

### 🖥️ Local Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/gym-management-flask.git
   cd gym-management-flask
   ```

2. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file and add your MongoDB URI:

   ```
   MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/gym
   ```

5. **Run the app:**

   ```bash
   flask run
   ```

   Open your browser at: [http://localhost:5000](http://localhost:5000)

---

## 🌐 Deployment on Render

1. Push your code to GitHub.
2. Create a new **Web Service** on [Render.com](https://render.com).
3. Set the **Build Command**:

   ```
   pip install -r requirements.txt
   ```
4. Set the **Start Command**:

   ```
   gunicorn app:app
   ```
5. Add environment variable `MONGO_URI` with your MongoDB connection string.

---

## 📁 Project Structure

```
gym-management/
├── templates/             # HTML templates
│   └── *.html
├── static/                # CSS/JS/Images
├── app.py                 # Main Flask app
├── requirements.txt       # Python dependencies
├── README.md
└── .env                   # MongoDB URI (not committed)
```

---

## 🛠️ Tools Used

* Flask
* PyMongo
* MongoDB Atlas
* Bootstrap
* Render (Deployment)

---

## 🧑‍💻 Author

**Fazil Imaad**
📧 Contact: [LinkedIn](https://linkedin.com/in/yourprofile)
💻 GitHub: [https://github.com/f4zill](https://github.com/f4zill)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
