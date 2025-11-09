from flask import Flask, jsonify
import mysql.connector
import psutil
import platform
import time
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql-db",        # same as docker-compose service name
        user="vatsal",
        password="vatsal123",
        database="stattracker"
    )

@app.route('/')
def home():
    return "Flask app connected to MySQL successfully!"

@app.route('/create_table')
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_stats (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cpu_usage FLOAT,
            memory_usage FLOAT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Table created successfully"})

@app.route('/add_stats')
def add_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    cursor.execute(
        "INSERT INTO system_stats (cpu_usage, memory_usage) VALUES (%s, %s)",
        (cpu_usage, memory_usage)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "System stats added!"})

@app.route('/stats')
def stats():
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "uptime_hours": round((time.time() - psutil.boot_time()) / 3600, 2)
    }
    return jsonify(system_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
