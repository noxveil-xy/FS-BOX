import socket


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self):
        set_ip = input(f"IP: ")
        set_port = int(input(f"PORT: "))

        self.client.connect((set_ip, set_port))
        print(f"Успешное подключение!")

        self.client.close()


client = Client()
client.connect()