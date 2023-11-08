import socket

# Server configuration
server_ip = '127.0.0.1'  # Change to your server's IP address
server_port = 12345      # Change to your desired port number
buffer_size = 1024

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Listening on {server_ip}:{server_port}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")
print("Make change in server.py")

# Receive the file
received_file = open('received_file.txt', 'wb')
while True:
    data = client_socket.recv(buffer_size)
    if not data:
        break
    received_file.write(data)

# Close the sockets and the file
received_file.close()
client_socket.close()
server_socket.close()

## Add comment