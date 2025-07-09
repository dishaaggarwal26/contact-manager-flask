from flask import Flask, render_template, request, redirect, url_for ,flash
import pymysql , re
import pymysql.cursors
from config import db_config, secret_key

app = Flask(__name__)
app.secret_key= secret_key
#for email validation through backend
def isvalidemail(email):
    pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    return re.match(pattern,email)

def get_db_connection():
    return pymysql.connect(host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    db=db_config["db"],
    cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM contacts')
        contacts = cursor.fetchall()
    conn.close()
    return render_template('index.html',contacts=contacts)

@app.route('/add',methods=('GET','POST'))
def add():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        email =request.form['email']
        phone = request.form['phone']

        if not isvalidemail(email):
            flash("invalid email format, please enter a valid email")
            return render_template('add.html')
        
        conn = get_db_connection()
        with conn.cursor() as cursor:
            # Check for existing email or phone
            cursor.execute('SELECT * FROM contacts WHERE email = %s OR phone = %s', (email, phone))
            existing = cursor.fetchone()

            if existing:
                flash('Email or Phone number already registered. Please use different details.')
                conn.close()
                return render_template('add.html')
            
            cursor.execute('INSERT INTO contacts (first_name, last_name, address,email,phone) VALUES (%s,%s,%s,%s,%s)',(first_name,last_name,address,email,phone))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/update/<int:id>',methods=('GET','POST'))
def update(id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM contacts WHERE id = %s',(id,))
        contact = cursor.fetchone()

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name =request.form['last_name']
        address = request.form['address']
        email = request.form['email']
        phone = request.form['phone']

        if not isvalidemail(email):
            flash("invalid email format, please enter a valid email")
            return render_template('update.html',contact=contact)
        
        with conn.cursor() as cursor:
            # Check if email or phone already exists for a different id
            cursor.execute('SELECT * FROM contacts WHERE (email = %s OR phone = %s) AND id != %s', (email, phone, id))
            existing = cursor.fetchone()

            if existing:
                flash('Email or Phone number already registered. Please use different details.')
                conn.close()
                return render_template('update.html', contact=contact)
            
            cursor.execute('UPDATE contacts SET first_name=%s, last_name=%s,address=%s,email=%s,phone=%s WHERE id=%s',(first_name,last_name,address,email,phone,id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn.close()
    return render_template('update.html',contact=contact)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM contacts WHERE id = %s',(id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)
