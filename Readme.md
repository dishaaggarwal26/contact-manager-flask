# Contact Manager (Flask + MySQL)

This is a simple web-based Contact Manager application built using:
- **Flask** (Python) for the backend
- **MySQL** as the database
- **Jinja2** for templating
- **Tailwind CSS** for frontend styling

## 💡 Features

✅ View all contacts  
✅ Add new contacts  
✅ Update existing contacts  
✅ Delete contacts

---

## 🚀 How to Run

### 1️⃣ Clone this repository

```bash
git clone https://github.com/dishaaggarwal26/contact-manager-flask.git
cd contact-manager-flask
```

### 2️⃣ Install Python dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Setup MySQL database
- Create a database named contactdb in your MySQL Workbench (or using CLI).

- Create a table named contacts:

```bash
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    address VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);
```
- Create a `config.py` file in the root directory with the following content:

db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "your_password_here",
    "db": "contactdb",
    "cursorclass": "pymysql.cursors.DictCursor"
}

 ### 4️⃣ Run the application

 ```bash
 python app.py
```
Open your browser and go to: http://127.0.0.1:5000/

<!-- ## 🎥 Demo Video
👉 [Click here to watch the demo video]() -->

## ✨ Author
Disha Aggarwal

## ⭐ License
This project is open-source and free to use for educational purposes.

