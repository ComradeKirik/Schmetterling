import socket

def conn_close(sock: socket.socket):
    sock.close()
    print('Соединение разорвано')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Настройка сокета
sock.connect(('localhost', 50500)) # Выделение порта под сокет

while True:
    message = input()
    if message == 'quit': # Проверка на разрыв соединения
        conn_close(sock)
    sock.send(bytes(message, encoding='UTF-16')) 
    data = sock.recv(1024)
    print('Возвращенное сообщение:', data.decode(encoding='UTF-16'))




# Я почти все сделал по основному (я про долги) поэтому сейчас начну +- завозить кода :)