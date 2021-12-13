#!/usr/bin/env python3
from rplidar import RPLidar
import time

#default port
PORT_NAME = '/dev/ttyUSB0'

#info on/off
help = True

#connect
def RPconnect(PORT_NAME):
	lidar = RPLidar(PORT_NAME)
	return lidar

#measure scan rate
def measureRate(PORT_NAME):
	if help == True:
		print('''
			Usage: measureRate(PORT_NAME)
		''')
	lidar = RPconnect(PORT_NAME)
	old_t = None
	data = []
	try:
		print('Ctrl-C to stop')
		for _ in lidar.iter_scans():
			now = time.time()
			if old_t is None:
				old_t = now
				continue
			delta = now - old_t
			print('%.2f Hz, %.2f RPM' % (1/delta, 60/delta))
			data.append(delta)
			old_t = now
	except KeyboardInterrupt:
		print('Stoping, Computing mean...')
		lidar.stop()
		lidar.disconnect()
		delta = sum(data)/len(data)
		print('Mean: %.2f Hz, %.2f RPM, %.2f Points/Min, %.2f Points/Sec' % (1/delta, 60/delta, (60/delta)*360, ((60/delta)*360)/60))

#record measurements
def measure(PORT_NAME, file):
	if help == True:
		print('''
			Usage: measure(PORT_NAME, file)
		''')
	lidar = RPLidar(PORT_NAME)
	outfile = open(file, 'w')
	try:
		print(f'Recording measurements @ {file}')
		for measurment in lidar.iter_measurments():
			line = '\t'.join(str(v) for v in measurment)
			outfile.write(line + '\n')
	except KeyboardInterrupt:
		print('Stoping.')
	lidar.stop()
	lidar.disconnect()
	outfile.close()
