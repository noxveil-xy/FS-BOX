#ИМПОРТЫ ------------------------------
import os
import sys

from client.client import client_obj
from server.server import cr_server


#ТОЧКА ВХОДА ---------------------------------------------------------------
if __name__ == "__main__":
    try:

        match sys.argv[1]:
            case "-server":
                cr_server.set_value()
                cr_server.create_server()
            case "-client":
                client_obj.connect()
            case _:
                print("Не подходящее значение..")


    #ОБРАБОТКА ОШИБОК---------------------------------------------------------
    except IndexError:
        print(f"\nОшибка: нужно задать параметр (-sever / -client).\n")
    except KeyboardInterrupt:
        print(f"\nЗавершение..\n")
    except Exception as err:
        print(f"\nПроизошла неожиданная ошибка: {err}\n")


