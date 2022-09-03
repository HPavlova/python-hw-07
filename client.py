from email import message
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8080


def run_client(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')
        # message = input('--> ')
        message = input(f'Enter your message: ')

        while message.lower().strip() != 'end':
            sock.send(message.encode())
            response = sock.recv(1024)
            print(f'Response data: {response.decode()}')
            message = input('--> ')

    print(f'Data transfer completed')
    sock.close()


if __name__ == '__main__':
    run_client(TCP_IP, TCP_PORT)
