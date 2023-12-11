from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __get_content(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.split(current_dir)[0]
        root_dir = os.path.split(src_dir)[0]
        filepath = os.path.join(root_dir, os.path.normpath('src'), os.path.normpath('Homework1'), 'index.html')
        if os.path.isfile(filepath):
            with open(file=filepath, mode='r', encoding='utf-8') as sql_file:
                line = sql_file.read()
        return line

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        page_content = self.__get_content()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
