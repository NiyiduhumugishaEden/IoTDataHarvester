import serial
import requests

ser = serial.Serial(
    port='/dev/ttyACM0',  # Change this to your port number
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

while True:
    temperature= ""  # Initialize distance as an empty string

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()

        with open("data.txt", "a") as file:
            file.write(line + "\n")
        
        temperature += line + "\n"

    if temperature.strip() != "":
        formData = {"device": "EdenDevice", "temperature": temperature}
        HTTP_Request = requests.post("http://insecure.benax.rw/iot/", data=formData)

        if HTTP_Request:
            HTTP_Response = HTTP_Request.text
            print(HTTP_Response)
