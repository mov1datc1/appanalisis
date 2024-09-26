import sqlite3
from datetime import datetime, timedelta
import random

# Crear conexión con la base de datos
conn = sqlite3.connect('../db/dummy_data.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS operations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operation_name TEXT NOT NULL,
        equipment_status TEXT NOT NULL,
        energy_consumption REAL NOT NULL,
        maintenance_status TEXT NOT NULL,
        report_date TEXT NOT NULL
    )
''')

# Datos simulados
equipments = ['HVAC System 1', 'Electric Circuit 3', 'Water Pump 2', 'Fire Safety System']
statuses = ['Running', 'Idle', 'Maintenance Needed']
maintenance_statuses = ['On Schedule', 'Maintenance Needed', 'Delayed']

start_date = datetime.now() - timedelta(days=90)  # Fecha de inicio: hace 3 meses
dummy_data = []

# Generar datos para los últimos 3 meses
for i in range(90):  # Un registro por día
    for equipment in equipments:
        date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
        status = random.choice(statuses)
        energy_consumption = round(random.uniform(50.0, 200.0), 2)  # Consumo aleatorio
        maintenance_status = random.choice(maintenance_statuses)
        dummy_data.append((equipment, status, energy_consumption, maintenance_status, date))

# Insertar datos simulados
cursor.executemany('''
    INSERT INTO operations (operation_name, equipment_status, energy_consumption, maintenance_status, report_date)
    VALUES (?, ?, ?, ?, ?)
''', dummy_data)

conn.commit()
conn.close()
