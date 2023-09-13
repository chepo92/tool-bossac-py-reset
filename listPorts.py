import serial.tools.list_ports
ports = []
for port in serial.tools.list_ports.comports():
    ports.append(port.device)
print(ports)


