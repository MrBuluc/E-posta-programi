"""https://myaccount.google.com/lesssecureapps"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = input("Gönderici e-postayı giriniz:")

parola = input("Gönderici e-posta parolasını giriniz:")

mesaj["To"] = input("Alıcı e-postayı giriniz:")

mesaj["Subject"] = input("Konuyu giriniz:")

yazi = input("Mesajı girin:")

mesaj_govdesi = MIMEText(yazi, "plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)

    mail.ehlo()

    mail.starttls()

    mail.login(mesaj["From"], parola)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

    print("Mail başarıyla gönderildi...")

    mail.close()

except:
    sys.stderr.write("Mail göndermesi başarısız oldu.")
    sys.stderr.flush()