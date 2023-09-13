import serial
from time import sleep
import serial.tools.list_ports

def TouchSerialPort(port, baudrate):
    print("Forcing reset using %dbps open/close on port %s" % (baudrate, port))
    try:
        print("Open")
        s = serial.Serial(
            port=port, 
            baudrate = baudrate
            #parity=0,
            #stopbits=1,
            #bytesize=8,
            #timeout=1
        )

        print("DTR")
        s.setDTR(False)
        print("Close")
        s.close()
    except:  # pylint: disable=bare-except
        print("Could not touch")
        pass
    sleep(0.4)  # DO NOT REMOVE THAT (required by SAM-BA based boards)



if __name__ == '__main__':
    ports = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.device)
    print("Avaliable ports:")
    print(ports)
    if len (ports)>0: 
        print("Using first port:")
        print(ports[0])
        TouchSerialPort(ports[0], 1200) # '/dev/ttyACM0' '/dev/ttyUSB0'
        print("Now try to upload your firmware")
    else:
        print("No ports found")
    
