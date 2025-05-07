from flask import Flask
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

app = Flask(__name__)

@app.route("/")
def hello():
    db = mysql.connector.connect(
        user=os.getenv("DB_USER"),
        host=os.getenv("DB_HOST"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

    cursor = db.cursor()
    cursor.execute("SELECT 'Hello from Flask and MySQL!'")
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)