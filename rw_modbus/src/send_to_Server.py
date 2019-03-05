# library to send to HTTP server
import socket

# the ip and port of the server where the message will be send
SERVER_IP = '192.168.168.11'
SERVER_PORT = 6101


BUFFER_SIZE = 2048



# creation of socket to connect to the server
def create_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return server_socket

def send_data(data):
    s=create_socket()
    s.connect(SERVER_IP,SERVER_PORT)
    s.sendall(data)
    response = s.recv(1024)

    print('Recieved ',  repr(response))
