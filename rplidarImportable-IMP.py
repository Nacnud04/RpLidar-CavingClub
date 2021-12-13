import sys
from rplidar import RPLidar

def connect(port):
    lidar = RPLidar(port)
    info = lidar.get_info()
    print(info)
    health = lidar.get_health()
    print(health)

# Number - Number of scans
# File - File for raw data to be output to (Time, quality, angle, distance)
# Type - How the file is to be written (eg: 'w+' - Write fresh, 'a+' - Append, etc.)

#Scan a certain number of times
def scanNum(number, file, type):
    rawfile = open(file, 'w+')
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i, len(scan)))
#        print(f'Quality, Angle, Distance : {scan}')
        for datapoint in scan:
            rawfile.write(f'{datapoint}\n')
        if i > (int(number)-2):
            break

#Scan only once
#Oftentimes yields incomplete scans due to the nature of doing only one scan
def scanOnce(file, type):
    rawfile = open(file, type)
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i, len(scan)))
#        print(f'Quality, Angle, Distance : {scan}')
        for datapoint in scan:
            rawfile.write(f'{datapoint}\n')
        break

#Scan until the program is killed or an error occurs
def scanUntilEx(file, type):
    #DO NOT CALL THIS FUNCTION UNLESS IN A EASILY KILLABLE FORMAT (EG. THREADING)
    #WILL RUN FOREVER
    rawfile = open(file, type)
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i, len(scan)))
#        print(f'Quality, Angle, Distance : {scan}')
        for datapoint in scan:
            rawfile.write(f'{datapoint}\n')

def stopLidar():
    lidar.stop()
    lidar.stop_motor()

def disconnect():
    lidar.disconnect()
