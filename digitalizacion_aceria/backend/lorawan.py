import serial

def read_sensor_data():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    data = ser.readline().decode('utf-8').strip()
    return float(data)