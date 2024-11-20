
#--------------------------------------------------

import socket
import threading

#--------------------------------------------------

def send_message(message, socket, address):
    socket.sendto(message.encode(), address)

def receive_messages(socket):
    while True:
        data, _ = socket.recvfrom(1024)
        print(f"\nReceived: {data.decode()}")

def start_client(rendezvous_ip):
    print("connecting to rendevouz...")
    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_message("hello, rendezvous!", tmp_socket, (rendezvous_ip, 5555))

    print("wainting for answer...")
    other_address, _ = tmp_socket.recvfrom(1024)
    other_ip, other_port = other_address.decode().split(':')
    other_port = int(other_port)
    print(f"my partner is {other_ip}:{other_port}")

    print(f"connecting...")
    print(f"connected to {other_ip}:{other_port}")
    threading.Thread(target=receive_messages, args=(tmp_socket,)).start()

    print("Enter message and press enter")
    while True:
        message = input()
        send_message(message, tmp_socket, (other_ip, other_port))

#--------------------------------------------------

if __name__ == "__main__":
    rendezvous_server_ip = input("Enter rendezvous server ip: ")
    start_client(rendezvous_server_ip)

#--------------------------------------------------
