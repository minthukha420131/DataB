import socket
import pymongo

class Tcp_server():

    def __init__(self):
        self.ip_address = 'localhost'
        self.port = 9698
        self.connection = pymongo.MongoClient(self.ip_address, 27017)
        self.database = self.connection['ncc_dip2']
        self.collection = self.database['user_info']

    def run_server(self):
        main_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main_server.bind((self.ip_address, self.port))
        main_server.listen(5)
        print(f"Server is running on ip : {self.ip_address} and port : {self.port}")

        try:
            while True:
                conn, addr = main_server.accept()
                print(f"The client is connecting with {addr[0]}, {addr[1]}")
                self.handle_data(conn)

        except Exception as err:
            print(err)

    def handle_data(self, client_info):
        with client_info as sock:
            encode_data = sock.recv(1024)
            decode_data = encode_data.decode('utf-8')
            if decode_data.lower() == 'gad':
                for i in self.collection.find({}, {'_id': 0}):
                    print(i)
                    to_clt = bytes("You requested function on server", 'utf-8')
                    sock.send(to_clt)

            else:
                print(f"The client request is {decode_data}")

                to_client = f"Server Got your request :> {decode_data} "
                sent_me = bytes(to_client, 'utf-8')
                sock.send(sent_me)

if __name__ == '__main__':
    tcp_server = Tcp_server()
    tcp_server.run_server()
