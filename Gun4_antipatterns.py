class GodObject:
    def __init__(self):
        self.database = "Database Connection"
        self.logger = "Logging System"
        self.api_manager = "API Manager"

    def perform_operations(self):
        print("Tüm işlemleri burada yapıyorum.")

class Database:
    def connect(self):
        print("Veritabanına bağlanıldı.")

class Logger:
    def log(self, message):
        print(f"Log: {message}")

class APIManager:
    def send_request(self):
        print("API isteği gönderildi.")

##SPAGETTİ
def hesapla(a, b):
    if a > 0:
        if b > 0:
            return a * b
        else:
            return a + b
    else:
        if b > 0:
            return b - a
        else:
            return a - b

def carp(a, b):
    return a * b

def topla(a, b):
    return a + b

def cikart(a, b):
    return b - a
#ÇÖZÜM
def hesapla(a, b):
    if a > 0 and b > 0:
        return carp(a, b)
    elif a > 0:
        return topla(a, b)
    elif b > 0:
        return cikart(a, b)
    else:
        return a - b

#COPY PASTE
def dikdortgen_alan(en, boy):
    return en * boy

def kare_alan(kenar):
    return kenar * kenar


def alan_hesapla(*boyutlar):
    if len(boyutlar) == 1:  # Kare
        return boyutlar[0] ** 2
    elif len(boyutlar) == 2:  # Dikdörtgen
        return boyutlar[0] * boyutlar[1]

#MAGIC NUMBERS

if yas > 18:
    print("Yetişkin.")

#ÇÖZÜM

MIN_YETISKIN_YASI = 18
if yas > MIN_YETISKIN_YASI:
    print("Yetişkin.")

#HARDCODING


def baglan():
    return "postgres://admin:password@localhost/db"

#ÇÖZÜM

import os

def baglan():
    return os.getenv("DATABASE_URL")




#PREMATURE OPTIMIZATION

def uzun_liste_olustur():
    return [x * 2 for x in range(1, 1000000) if x % 3 == 0]

#ÇÖZÜM

def uzun_liste_olustur():
    for x in range(1, 1000000):
        if x % 3 == 0:
            yield x * 2  # Gerektiğinde hesaplanır"""
