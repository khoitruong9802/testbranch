import socket

# Client configuration
server_ip = '127.0.0.1'  # Change to the server's IP address
server_port = 12345      # Change to the server's port number
buffer_size = 1024

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Send the file
file_to_send = open('file_to_send.txt', 'rb')
data = file_to_send.read(buffer_size)
while data:
    client_socket.send(data)
    data = file_to_send.read(buffer_size)
print("Make change in client.py")
# Close the socket and the file
client_socket.close()
file_to_send.close()
