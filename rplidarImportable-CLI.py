import sys
from rplidar import RPLidar

if sys.argv[1] == '-h':
    print('''
        Usage: python3 test.py {portname} {scantype} {#scans/outfile/type} {outfile/rate}
            -n = Scan a certain number of times then stop
              eg. -n 15 outfile.txt
            -o = Scan once then stop
              eg. -o outfile.txt
            -e = Scan until exception
              eg. -e outfile.txt
    ''')
    sys.exit()

lidar = RPLidar(sys.argv[1])

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

if sys.argv[2] == '-n':
    rawfile = open(sys.argv[4], 'w+')
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i, len(scan)))
#        print(f'Quality, Angle, Distance : {scan}')
        for datapoint in scan:
            rawfile.write(f'{datapoint}\n')
        if i > (int(sys.argv[3])-2):
            break

elif sys.argv[2] == '-o':
    rawfile = open(sys.argv[3], 'w+')
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i, len(scan)))
#        print(f'Quality, Angle, Distance : {scan}')
        for datapoint in scan:
            rawfile.write(f'{datapoint}\n')
        break

elif sys.argv[2] == '-e':
    rawfile = open(sys.argv[3], 'w+')
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i, len(scan)))
#        print(f'Quality, Angle, Distance : {scan}')
        for datapoint in scan:
            rawfile.write(f'{datapoint}\n')

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
