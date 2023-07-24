from flask import Flask, render_template, request
import pandas as pd
import mysql.connector
conn = mysql.connector.connect (host='localhost', password='***', user='root')



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']

    data = {'Name': [name], 'Age': [age]}
    df = pd.DataFrame(data)

    try:
        # Load existing data from the Excel file
        existing_data = pd.read_excel('userdata.xlsx')
        updated_data = pd.concat([existing_data, df], ignore_index=True)
        updated_data.to_excel('userdata.xlsx', index=False)
    except FileNotFoundError:
        # Create a new Excel file if it doesn't exist
        df.to_excel('userdata.xlsx', index=False)

    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run()
