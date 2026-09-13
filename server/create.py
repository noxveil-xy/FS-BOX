import socket


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.local_ip = None
        self.port = None


    def set_value(self):
        get_host = socket.gethostname()
        self.local_ip = socket.gethostbyname(get_host)
        self.port = int(input(f"Set the port: "))


    def create_server(self):
        self.server.bind((self.local_ip, self.port))
        self.server.listen(5)
        user, adress = self.server.accept()
        print(f"{user} {adress}")

        self.server.close()



cr_server = Server()
cr_server.set_value()
cr_server.create_server()