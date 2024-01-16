# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import os
# from dotenv import load_dotenv
from django.core.mail import send_mail
from django.conf import settings


def send_email(title):
    send_mail('Статья', f'Количество просмотров статьи {title} более 15', settings.EMAIL_HOST_USER,
              [settings.DEFAULT_RECIPIENT, ])

#
# class Email:
#     def __init__(self):
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         root_dir = os.path.split(current_dir)[0]
#         print(root_dir)
#         filepath = os.path.join(root_dir, '.env')
#         if os.path.exists(filepath):
#             load_dotenv(filepath)
#         self.my_email = os.getenv('EMAIL')
#         self.my_pass = os.getenv('PASSWORD')
#         print(self.my_pass)
#         self.smtp_server = smtplib.SMTP("smtp.yandex.ru", 465)
#         self.smtp_server.starttls()
#         self.smtp_server.login(self.my_email, self.my_pass)
#         print(self.my_email, self.my_pass)
#
#     def send(self):
#         # Создание объекта сообщения
#         msg = MIMEMultipart()
#
#         # Настройка параметров сообщения
#         msg["From"] = self.my_email
#         msg["To"] = self.my_email
#         msg["Subject"] = "Congratulations!"
#
#         # Добавление текста в сообщение
#         text = "Hi, your post is viewed more than 100!"
#         msg.attach(MIMEText(text, "plain"))
#
#         # Отправка письма
#         self.smtp_server.sendmail(self.my_email, self.my_email, msg.as_string())
#
#         # Закрытие соединения
#         self.smtp_server.quit()
#         # send_mail('subject', 'message', self.my_email,['andrey.yuryev@gmail.com',], auth_user=self.my_email, auth_password=self.my_pass)
