import serial
import sqlite3
import requests

# Connect to the SQLite database
conn = sqlite3.connect("heart_rate_data.db")
cursor = conn.cursor()

# Create a table to store temperature data if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS temperature_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device TEXT,
        temperature REAL,
        status INTEGER DEFAULT 0
    )
''')
conn.commit()

# Connect to the microcontroller
ser = serial.Serial(
    port='/dev/ttyACM1',  # Change this to your port number
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()

        # Store data in the SQLite database with status set to 0 by default
        cursor.execute("INSERT INTO temperature_data (device, temperature) VALUES (?, ?)", ("EdenDevice", line))
        conn.commit()
        print(f"Temperature data saved to database: {line}")

        # Attempt to upload the data to a server
        formData = {"device": "EdenDevice", "temperature": line}
        HTTP_Request = requests.post("http://example.com/upload", data=formData)
       

        if HTTP_Request.status_code == 200:
            # If the upload is successful, update the status to 1
            cursor.execute("UPDATE temperature_data SET status = 1 WHERE temperature = ?", (line,))
            conn.commit()
            print(f"Temperature data with value {line} uploaded successfully.")
