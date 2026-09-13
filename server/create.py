import socket


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.local_ip = None
        self.port = None


    def set_value(self):
        self.local_ip = input(f"Set the ip: ")
        self.port = int(input(f"Set the port: "))


    def create_server(self):
        self.server.bind((self.local_ip, self.port))
        self.server.listen(5)
        user, adress = self.server.accept()
        print(f"{user} {adress}")

        data = user.recv(1024).decode("utf-8")
        #get_message = data.decode("utf-8")
        print(f"+1 сообщение")
        print(data)

        self.server.close()


cr_server = Server()
cr_server.set_value()
cr_server.create_server()