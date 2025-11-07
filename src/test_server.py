import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Инициализация сокета
sock.bind(('', 50500)) # Привязка сокета к порту 8888
sock.listen(10) # Количество человек в очереди на подключение
print('Тестовый сервер запущен. Нажмите Ctrl+C для выключения')

while True:
    conn, addr = sock.accept() # Принимаем и сохраняем данные от клиента: сокет и адрес
    print(f'Успешное соединение с пользователем {addr}!')
    data = conn.recv(1024) # Получаем данные от пользователя по 1024 КБ
    print('Получено:', data.decode('UTF-16'))
    conn.send(bytes(f'Hello {addr[0]}!', encoding='UTF-16'))

    conn.close()
