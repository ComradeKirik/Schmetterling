import socket
from json_system import writefile
import time




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

while True:
    inputed = input("Введите сообщение: ")
    if inputed == "отсоединение":
        sock.close()
        break

    t = time.time()
    filename = f"{t}.json"
    print(f"{t} - время отправки")
    filepath = writefile(f"send{t}", "message", "test", "test2", inputed + "艾")

    # Отправляем имя файла
    sock.send(filename.encode("UTF-8"))

    # Отправляем содержимое файла
    with open(filepath, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                sock.close()
                break
            sock.send(data)


    print("Сообщение отправлено")