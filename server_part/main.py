import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print("Тестовый сервер запущен. Нажмите Ctrl+C для выключения")

# Создаем папку если нет
os.makedirs("packets", exist_ok=True)

while True:
    conn, addr = sock.accept()
    print("Соединено: ", addr)

    try:
        # Получаем имя файла
        filename = conn.recv(1024).decode("UTF-8").strip()
        print(f"Получение файла: {filename}")

        file = open("packets/" + filename, "wb")
        while True:
            data = conn.recv(1024)
            if "艾" in data:
                break
            file.write(data)
        file.close()
        print("Пакет получен")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()