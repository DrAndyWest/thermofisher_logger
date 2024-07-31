#!/usr/bin/python
""" Serial communication for the Thermo Scientific RadEye GN+ radiation detector.
    - Writes output to a log file
"""


import serial
import time
import datetime
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', nargs='?', default="/dev/ttyUSB0", type=str, help="port of serial->usb cable, e.g. --port /dev/ttyUSB0")
    args = parser.parse_args()
    return args
    

def create_log_file():
    current_time = datetime.datetime.now()
    filename = "G10_STS_" + current_time.strftime("%Y%m%d_%H-%M") + ".log"
    return filename

def logdata(outfile, data):
    out=data.split(' ')
    if len(out) == 11:
        elapsed_time = time.time() - start_time
        dose_rate = int(out[1])/100 # 1/100 Rad->Sievert
        print(f'Time (s): {elapsed_time:.2f}, Dose Rate: {dose_rate} uSv/hr')

        with open(outfile,'a') as f: # append to the file in byte mode
            f.write(f'{elapsed_time:.2f},{dose_rate}\n')

if __name__ == "__main__":
    input_args = parse_args()
    serial_port = input_args.port
    
    logfile = create_log_file()  #"radeye_bytesSim.log"
    
    # Establish a serial port connection IAW specification on page 2-1
    controlBytes=['\x02','\x03', "b'\x02'"]
    ser = serial.Serial(
        port=serial_port,
        baudrate=9600,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS,
        xonxoff=False,
        rtscts=False,
        dsrdtr=True
    )
    
    # if the connection was left open, then close it.
    if (ser.isOpen()):
        ser.close()
    # Open the serial connection
    ser.open()
    time.sleep(1.5)
    
    # Send the commands for the device to repeateadly send values every second.
    ser.write(b'00')
    byte = ser.read(1)
    time.sleep(0.5)
    
    # This is the command to make the device start streaming sensor values
    cmd=b'/X1\r\n'
    ser.write(cmd)
    byte = ser.read(1)
    time.sleep(.1)


    start_time = time.time()
    # Start the big while loop
    while True:

        # Collecting data from the Radeye
        out = ''
        while ser.inWaiting() > 0: # While there is a byte in the buffer waiting to be read.
            byte = ser.read().decode('utf-8') # Read one byte at a time. Readline was not a good solution as it included control bytes.
            if (byte not in controlBytes): # this prevents control bytes from being added to the output.
                out += byte

        logdata(logfile, out)
        time.sleep(1.0)
        
       
