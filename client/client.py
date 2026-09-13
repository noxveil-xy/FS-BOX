import socket
import os


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self):
        set_ip = input(f"IP: ")
        set_port = int(input(f"PORT: "))

        self.client.connect((set_ip, set_port))
        print(f"Успешное подключение!")

        user_name = os.getlogin()
        message = input(f"{os.getlogin()}: ")
        res_message = f"[{user_name}] {message}".encode("utf-8")
        self.client.send(message)
        print("Сообщение отправлено!")


        self.client.close()


client = Client()
client.connect()
