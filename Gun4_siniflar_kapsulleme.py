"""class Araba:
    def __init__(self, marka, model, yil):
        
        self.__marka = marka#private
        self.__model = model
        self.__yil = yil
    
    
    def get_marka(self):
        return self.__marka
    
    def get_model(self):
        return self.__model
    
    def get_yil(self):
        return self.__yil
    
    
    def set_marka(self, marka):
        if marka != "":
            self.__marka = marka
        else:
            print("Marka geçersiz!")
    
    def set_model(self, model):
        if model != "":
            self.__model = model
        else:
            print("Model geçersiz!")
    
    def set_yil(self, yil):
        if yil > 1900:
            self.__yil = yil
        else:
            print("Yıl geçersiz!")


araba = Araba("Volkswagen", "Polo", 2024)




print(araba.get_marka())  
print(araba.get_model())  
print(araba.get_yil())    


araba.set_marka("BMW")
print(araba.get_marka())  


araba.set_yil(1800)  

###
"""
class BankaHesabi:
    def __init__(self, ad, bakiye):
        self.ad = ad               # Genel (public)
        self._hesap_numarasi = 1234 # Korumalı (protected)
        self.__bakiye = bakiye     # Özel (private)
    
    #setter
    # Bakiye güncelleme (kontrollü erişim)
    def para_ekle(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar #bakiye=bakiye+miktar
            return f"Yeni bakiye: {self.__bakiye}"
        return "Geçersiz miktar!"

    #getter
    # Bakiye sorgulama (kontrollü erişim)
    def bakiye_goster(self):
        return f"Bakiye: {self.__bakiye}"

# Sınıfın kullanımı
hesap = BankaHesabi("Ahmet", 1000)

# Public özelliklere erişim
print(hesap.ad)  

# Protected özelliklere erişim (yine de erişilebilir)
print(hesap._hesap_numarasi) 


# Private özelliklere doğrudan erişim mümkün değil!
#print(hesap.__bakiye)  # Hata verir! 
nesne=BankaHesabi("alp",100)
print(nesne._BankaHesabi__bakiye)

# Private özelliğe kontrollü erişim
print(hesap.bakiye_goster())  
print(hesap.para_ekle(500))   

#Maaş bilgisi uygulaması
#isim bilgileri public olacak şekilde maaş bilgileri private olacak şekilde değişkenleri tanımlayalım
#getter, setter metotlarını kullanarak maaş bilgilerini dışarıdan görüntülenebilir ve değiştirilebilir yapalım
#isim ve maaş bilgilerini görüntüleyip, değiştirme işlemi yapalım
#Bitiş: 11:00