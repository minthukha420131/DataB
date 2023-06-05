import socket

class Tcp_client:

    def __init__(self, user_data):
        self.ip_address = 'localhost'
        self.port = 9698
        self.message = bytes(user_data, 'utf-8')


    def run_client(self):
        clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clt.connect((self.ip_address, self.port))

        clt.send(self.message)

        received_from_server = clt.recv(4096)

        recv_sms = received_from_server.decode("utf-8")
        print(recv_sms)


        clt.close()

if __name__ == '__main__':
    while True:
        user_data = input("Enter your request : ")
        client = Tcp_client(user_data)
        client.run_client()

