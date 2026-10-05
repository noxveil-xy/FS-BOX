#ИМПОРТ --------
import socket
import os
import time
import sys


#КЛАСС КЛИЕНТА ------------------------------------------------------------
class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.user_name = os.getlogin()


    #ОТПРАВКА И ПРИЕМ СООБЩЕНИЙ С СЕРВЕРА ---------------------------------------------
    def write_client(self, ip, port, user_server):
        while True:
            current_time = time.time()
            local_time = time.localtime(current_time)
            decode_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

            message = input(f"{user_server}@{ip}:{port}: ")
            res_message = f"[{decode_time}] [{self.user_name}] {message}"

            
            #ОТПРАВЛЯЕМ --------------------------------------
            self.client.send(res_message.encode("utf-8"))
            
            #ПОЛУЧАЕМ --------------------------------------
            data = self.client.recv(1024).decode("utf-8")


        self.client.close()


    #ПОДКЛЮЧЕНИЕ К СЕРВЕРУ --------------------------
    def connect(self):
        set_ip = input(f"Set the ip: ")
        set_port = int(input(f"Set the port: "))
        print()

        self.client.connect((set_ip, set_port))
        get_user_server = self.client.recv(1024).decode("utf-8")

        self.write_client(set_ip, set_port, get_user_server)


#СОЗДАНИЕ ОБЪЕКТА КЛИЕНТА ---
client_obj = Client()
