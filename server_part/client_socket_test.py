import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('localhost', 55000))  # подключаемся к серверному сокету
file = "packets/example.json"
while True:
    inputed = input()
    if inputed == "отсоединение":
        sock.close()  # закрываем соединение
        break
    sock.send(bytes(file, encoding='UTF-16'))  # отправляем сообщение
    with open(file, "rb") as f:

        data = sock.recv(1024)  # читаем ответ от серверного сокета
    print(data.decode('UTF-16'))
