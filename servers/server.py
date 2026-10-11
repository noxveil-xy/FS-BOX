#ИМПОРТЫ---------
import socket
import os

from servers.path import ROOT_PATH, PATH_FILES_SERVER
from storage.commands import comms


#КЛАСС СЕРВЕРА -----------------------------------------------------------
class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.get_user = os.getlogin()
        self.local_ip = None
        self.port = None
        self.status = None


    #ЗАДАЕМ ДАННЫЕ ДЛЯ ПРИВЯЗКИ К СОКЕТУ -----------
    def set_value(self):
        self.local_ip = input(f"Set the ip: ")
        self.port = int(input(f"Set the port: "))


    #РАБОТА С КАНАЛОМ ДОЧЕРНЕГО СОКЕТА КЛИЕНТА (ПРИЕМ СООБЩЕНИЙ) -------------
    def user_channel(self):

        while True:
            user, adress = self.server.accept()
            send_user = user.send(self.get_user.encode("utf-8"))

            status = f"[{self.get_user}@{self.local_ip}:{self.port}]: получено ✓\n"


            while user:
                data = user.recv(1024)
                if len(data) <= 1:
                    break
                else:
                    decode_data = data.decode("utf-8")
                    value_decode_data = decode_data.split(" ")[3]
                    print(decode_data)

                    
                    if value_decode_data == comms[1]:
                        server_res = f"{os.getcwd()}\n"
                    elif value_decode_data == comms[2]:
                        server_res = f"{os.listdir(PATH_FILES_SERVER)}\n"
                    else:
                        server_res = "ERR"

            
                    response_cl = user.send(server_res.encode("utf-8"))

        self.server.close()


    #СОЗДАНИЕ СОКЕТА И ПРИВЯЗКА IP + PORT -------------------------------------
    def create_server(self):
        self.server.bind((self.local_ip, self.port))
        print(f"\n[СЕРВЕР ЗАПУЩЕН: {self.local_ip}:{self.port}]\n")


        #ПОДКЛЮЧЕНИЯ ------------
        self.server.listen(5)
        self.user_channel()


#ОБЪЕКТ СЕРВЕРА -------
cr_server = Server()
