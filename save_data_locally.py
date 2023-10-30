import serial

ser = serial.Serial(
    port='/dev/ttyACM0',  # Change this to your port number
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

try:
    with open("data.txt", "a") as file:
        while True:
            if ser.in_waiting > 0:
                try:
                    line = ser.readline().decode('utf-8', errors='ignore').rstrip()
                    file.write(line + "\n")
                    print(line)  # Optionally, print the received line
                except UnicodeDecodeError:
                    print("Error decoding line, skipping...")
except KeyboardInterrupt:
    ser.close()  # Close the serial port when you interrupt the program (e.g., with Ctrl+C)
