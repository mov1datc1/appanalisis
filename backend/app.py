from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('db/dummy_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route to fetch operational data
@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    operations_data = conn.execute('SELECT * FROM operations').fetchall()
    conn.close()

    data_list = []
    for row in operations_data:
        data_list.append(dict(row))

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True)
