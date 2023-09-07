# echo-client.py

import socket,sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for input in sys.stdin:
        line = input.rstrip()
        if 'exit' == line:
            break
        s.sendall(line.encode())
        data = s.recv(1024)
        print(f"Received {data.decode()!r}")
