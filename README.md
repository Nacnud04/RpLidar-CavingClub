# How to use

## rplidar.py
- Base rplidar library.
- Do not pip install onto the device. Instead copy the library to the operating directory with the other programs.
- Pip installing will install a different version of the library which will not function correctly due to the weird revision of the rplidar device being used.

## lidarTests-IMP.py
- To be ran by importing into another python program.
- 2 functions - Measure scan rate, and record point data

## rplidarImportable-CLI.py
- To be directly used from the command line interface.
- ex: python3 rplidarImportable-CLI.py {portname} {scantype} {#scans/outfile/type} {outfile/rate}
- portname: the port on which the rplidar is operating from (should be /dev/ttyUSB0)
- scantype: can be -h, -n, -o, -e
   - -h is a help function, shows how the program is used
   - -n scans a certain number of times until it stops (eg. -n 15 outfile.txt)
   - -o scans once and then stops (eg. -o outfile.txt)
   - -e scans until an exception occurs (eg. -e outfile.txt)
   - -e will run forever. if using the CLI it can be easily stopped by using Command-C to stop the program from running.
   
## rplidarImportable-IMP.py
- The same as rplidarImportable-CLI.py just the the program is written as functions which can be imported into another program.
- More information in comments of program

## simpleRecord-CLI.py
- Records measurments to a given file. 
- Usage example: python3 simpleRecord-CLI.py outfile.txt
