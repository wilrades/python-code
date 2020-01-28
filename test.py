import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("error")

port = 80

try:
    host_ip =
    socket.gethostbyname(igraciastelkomuniversity.ac.id)
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

s.connect((host_ip, port))

print("ip:"+host_ip)
