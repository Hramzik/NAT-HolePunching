
#--------------------------------------------------

import socket
import threading

#--------------------------------------------------

all_clients = []

#--------------------------------------------------

def handle_client(client):
        if len(all_clients) == 0:
            print("got first client")
            all_clients.append(client)
            return

        print("got second client")
        print("sending ips...")
        all_clients.append(client)
        other_client = all_clients[0]
        tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tmp_socket.sendto(f"{client[0]}:{client[1]}"            .encode(), other_client)
        tmp_socket.sendto(f"{other_client[0]}:{other_client[1]}".encode(), client)
        print("done")

def start_rendezvous_server(host, port):

    # open socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"rendezvous server started on {host}:{port}")

    # wait for clients
    print("waiting for clients...")
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"blud {client_address[0]} sent some garbage:")
        print(data.decode())
        threading.Thread(target=handle_client, args=(client_address,)).start()

#--------------------------------------------------

if __name__ == "__main__":
    my_ip = input("Enter rendezvous server (my) ip: ")
    start_rendezvous_server(my_ip, 5555)

#--------------------------------------------------
