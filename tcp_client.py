import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
msg = client_socket.recv(1024)
msg1 = client_socket.recv(1024)
msg2 = client_socket.recv(1024)
msg3 = client_socket.recv(1024)
msg4 = client_socket.recv(1024)
msg5 = client_socket.recv(1024)
print(f"Message from server: {msg.decode()}")
print(f"Message from server: {msg1.decode()}")
print(f"Message from server: {msg2.decode()}")
print(f"Message from server: {msg3.decode()}")
print(f"Message from server: {msg4.decode()}")
print(f"Message from server: {msg5.decode()}")
client_socket.close()