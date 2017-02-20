import serial
from pynmea import nmea

'''
see: https://media.readthedocs.org/pdf/pynmea/latest/pynmea.pdf

gpgga.age_gps_data      gpgga.gps_qual          gpgga.num_sats
gpgga.altitude_units    gpgga.horizontal_dil    gpgga.parse
gpgga.antenna_altitude  gpgga.lat_direction     gpgga.parse_map
gpgga.check_chksum      gpgga.latitude          gpgga.parts
gpgga.checksum          gpgga.lon_direction     gpgga.ref_station_id
gpgga.geo_sep           gpgga.longitude         gpgga.sen_type
gpgga.geo_sep_units     gpgga.nmea_sentence     gpgga.timestamp

'''

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

def dec_to_deg(decimal):
    '''
    converts decimal format of latitude, longitude to string form
    '''
    deg = decimal.split('.')[0][:-2]
    minutes = decimal.split('.')[0][-2:] + '.' + decimal.split('.')[1]

    return deg, minutes


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
    if 'GPGGA' in raw_gps:
        gpgga.parse(raw_gps)
        if int(gpgga.gps_qual) == 1:
            lat_deg, lat_min = dec_to_deg(gpgga.latitude)
            long_deg, long_min = dec_to_deg(gpgga.longitude)
            print 'num sats:', gpgga.num_sats
            print 'gps quality: ', gpgga.gps_qual
            print 'lat: ', lat_deg + ' ' + lat_min + ' ' + gpgga.lat_direction
            print 'latraw: ', gpgga.latitude
            print 'long: ', long_deg + ' ' + long_min + ' ' + gpgga.lon_direction
            print 'lonraw: ', gpgga.longitude
            print '\n'
        else:
            print gpgga.gps_qual
        # print('all: ', gpgga.nmea_sentence)
