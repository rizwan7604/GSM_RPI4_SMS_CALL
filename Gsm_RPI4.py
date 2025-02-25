import serial
import time
import keyboard  # Requires sudo/root access on Linux

# Configure Serial Port for GSM
ser = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

def send_sms():
    ser.write(b'AT+CMGF=1\r')  # Set SMS mode
    time.sleep(1)
    ser.write(b'AT+CMGS="+91XXXXXXXXXX"\r')  # Replace with your number
    time.sleep(1)
    ser.write(b'Blue Bull Detected! Alert!\x1A')  # Message + End with Ctrl+Z (ASCII 26)
    time.sleep(3)
    print("SMS Sent!")

def make_call():
    ser.write(b'ATD+91XXXXXXXXXX;\r')  # Replace with your number
    time.sleep(10)  # Keep call active for 10 sec
    ser.write(b'ATH\r')  # Hang up
    print("Call Made!")

print("Press 's' to send SMS, 'c' to make a call, or 'q' to quit.")

while True:
    if keyboard.is_pressed('s'):
        send_sms()
        time.sleep(1)
    elif keyboard.is_pressed('c'):
        make_call()
        time.sleep(1)
    elif keyboard.is_pressed('q'):
        print("Exiting...")
        break
