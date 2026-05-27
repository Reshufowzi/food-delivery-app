
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="password",
    database="foodapp"
)

@app.route('/register', methods=['POST'])
def register():
    data = request.json

    cursor = db.cursor()

    query = "INSERT INTO users(name, email, password) VALUES(%s,%s,%s)"

    values = (
        data['name'],
        data['email'],
        data['password']
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message":"User Registered Successfully"})


@app.route('/login', methods=['POST'])
def login():
    data = request.json

    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE email=%s AND password=%s"

    values = (
        data['email'],
        data['password']
    )

    cursor.execute(query, values)

    user = cursor.fetchone()

    if user:
        return jsonify({"success":True})

    return jsonify({"success":False})


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
