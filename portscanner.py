import socket
import threading as thr

def scan_port(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target,port))
    if result ==0:
        service = socket.getservbyport(port)
        print(f"Port {port} OPEN - {service}")
        s.close

target = input("Enter target IP: ")

start_port = int(input("Enter first port in range: "))

finish_port = int(input("Enter last port in range: "))

print("Scanning: ", target)

for port in range (start_port, finish_port):
    thread=thr.Thread(target=scan_port,args=(port,))
    thread.start()