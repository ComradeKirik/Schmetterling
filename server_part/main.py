import socket
from json_system import readfile

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание сокета
sock.bind(('', 55000))  # Связывание сокета с портом, где он будет ожидать сообщения
sock.listen(10)  # Сколько может принимать сообщений
print("Тестовый сервер запущен. Нажмите Ctrl+C для выключения")
print(readfile("example"))

while True:
    conn, addr = sock.accept()
    print("Соединено: ", addr)
    data = conn.recv(1024)  # Получение пакетов данных от юзера, по 1024 байт
    print(f"Получено: {data.decode('UTF-16')}")
    conn.send(data)
    conn.close()