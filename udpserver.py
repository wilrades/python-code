import socket
UDP_IP = "127.0.0.1"
# UDP_IP = "10.20.160.35"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print(addr)
    print("pesan diterima:", data.decode())
