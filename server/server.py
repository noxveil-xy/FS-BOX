import socket


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.local_ip = None
        self.port = None


    def set_value(self):
        self.local_ip = input(f"Set the ip: ")
        self.port = int(input(f"Set the port: "))


    def user_channel(self):
        while True:
            user, adress = self.server.accept()

            while user:
                data = user.recv(1024)
                if len(data) <= 1:
                    break
                else:
                    decode_data = data.decode("utf-8")
                    print(decode_data)
        self.server.close()


    def create_server(self):
        self.server.bind((self.local_ip, self.port))
        print(f"\n[СЕРВЕР ЗАПУЩЕН: {self.local_ip}:{self.port}]\n")

        self.server.listen(5)
        self.user_channel()


cr_server = Server()
