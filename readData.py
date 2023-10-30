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
    while True:
        data = ser.readline()  # Read a line of data from the serial port
        if data:
            print(data.decode('utf-8').strip())  # Print the decoded data
except KeyboardInterrupt:
    ser.close()  # Close the serial port when you interrupt the program (e.g., with Ctrl+C)


# print("hello world ")
# print(ser.readline().decode('utf-8').rstrip())

# ser.flush()