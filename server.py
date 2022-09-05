import socket
from concurrent import futures

TCP_IP = '127.0.0.1'
TCP_PORT = 8080


def run_server(ip, port):
    def handle(sock: socket.socket, address: str):
        print(f'SERVER: Connection established {address}')
        while True:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(message)
            message = input('--> ')
            sock.send(message.encode())
        sock.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(2)
    print(f'Start echo server {server_socket.getsockname()}')
    with futures.ThreadPoolExecutor(2) as client_pool:
        try:
            while True:
                new_sock, address = server_socket.accept()
                client_pool.submit(handle, new_sock, address)
        except KeyboardInterrupt:
            print(f'Destroy server')
        finally:
            server_socket.close()


if __name__ == '__main__':
    run_server(TCP_IP, TCP_PORT)