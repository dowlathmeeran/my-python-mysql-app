from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql_host',
        user='mysql_user',
        password='mysql_password',
        database='mysql_db'
    )
    return connection

@app.route('/create', methods=['POST'])
def create():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO my_table (name) VALUES (%s)", (data['name'],))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Record created'}), 201

@app.route('/read', methods=['GET'])
def read():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM my_table")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(rows), 200

@app.route('/update', methods=['PUT'])
def update():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE my_table SET name = %s WHERE id = %s", (data['name'], data['id']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Record updated'}), 200

@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM my_table WHERE id = %s", (data['id'],))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Record deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
