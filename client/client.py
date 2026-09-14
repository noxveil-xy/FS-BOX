import socket
import os
import time


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.user_name = os.getlogin()

    def write_client(self, ip, port):
        while True:
            current_time = time.time()
            local_time = time.localtime(current_time)
            decode_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

            message = input(f"{self.user_name}@{ip}:{port}: ")
            res_message = f"[{decode_time}] [{self.user_name}] {message}"
            self.client.send(res_message.encode("utf-8"))

        self.client.close()


    def connect(self):
        set_ip = input(f"Set the ip: ")
        set_port = int(input(f"Set the port: "))
        print()

        self.client.connect((set_ip, set_port))
        self.write_client(set_ip, set_port)


client_obj = Client()
