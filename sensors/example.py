import serial
from pynmea import nmea


def set_up_gps():
    ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=9600,
        # parity=serial.PARITY_NONE,
        # stopbits=serial.STOPBITS_ONE,
        # bytesize=serial.EIGHTBITS,
        timeout=1
    )
    # counter=0
    return ser


def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv


port = set_up_gps()
gpgga = nmea.GPGGA()
while True:
    raw_gps = readlineCR(port)
    print(raw_gps)
    # gpgga.parse(raw_gps)
    # print('lat: ', gpgga.latitude, 'long: ', gpgga.longitude)
    # print('all: ', gpgga.nmea_sentence)

