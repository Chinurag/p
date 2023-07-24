import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Establish MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='hesoyam21',
    database='userdb'
)

# Create a cursor object
cursor = conn.cursor()

# Create a table for storing user data
create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL
    )
"""
cursor.execute(create_table_query)
conn.commit()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']

        # Check if the username already exists in the database
        check_username_query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(check_username_query, (username,))
        if cursor.fetchone():
            return render_template('signup.html', message='Username already exists. Please choose a different one.')

        # Insert user data into the database
        insert_user_query = "INSERT INTO users (username, email, password, name) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_user_query, (username, email, password, name))
        conn.commit()

        return redirect('/profile')

    return render_template('signup.html', message='')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Retrieve user data from the database
        select_user_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(select_user_query, (username, password))
        user = cursor.fetchone()

        if user:
            return redirect('/profile')

        return render_template('login.html', message='Invalid username or password.')

    return render_template('login.html', message='')


@app.route('/profile')
def profile():
    # Fetch all user data from the database
    select_all_users_query = "SELECT * FROM users"
    cursor.execute(select_all_users_query)
    users = cursor.fetchall()

    return render_template('profile.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)

# Close the cursor and the connection
cursor.close()
conn.close()
