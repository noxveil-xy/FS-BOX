#ИМПОРТЫ---------
import socket
import os


#КЛАСС СЕРВЕРА -----------------------------------------------------------
class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.local_ip = None
        self.port = None


    #ЗАДАЕМ ДАННЫЕ ДЛЯ ПРИВЯЗКИ К СОКЕТУ -----------
    def set_value(self):
        self.local_ip = input(f"Set the ip: ")
        self.port = int(input(f"Set the port: "))


    #РАБОТА С КАНАЛОМ ДОЧЕРНЕГО СОКЕТА КЛИЕНТА (ПРИЕМ СООБЩЕНИЙ) -------------
    def user_channel(self):
        while True:
            user, adress = self.server.accept()

            get_user = os.getlogin()
            send_user = user.send(get_user.encode("utf-8"))

            while user:
                data = user.recv(1024)
                if len(data) <= 1:
                    break
                else:
                    decode_data = data.decode("utf-8")
                    print(decode_data)
                    message = "ok"

                    # response_cl = user.send(message.encode("utf-8"))

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
