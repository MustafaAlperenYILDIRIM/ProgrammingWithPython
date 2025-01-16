##init

class Ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Soyad: {self.soyad}, Numara: {self.numara}"

ogrenci1 = Ogrenci("Ahmet", "Yılmaz", 123)
print(ogrenci1.bilgileri_goster())


#init olmadan - manuel

class Ogrenci:
    def __init__(self):  
        pass

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Soyad: {self.soyad}, Numara: {self.numara}"

# Nesne oluşturma
ogrenci1 = Ogrenci()
ogrenci1.ad = "Ahmet"
ogrenci1.soyad = "Yılmaz"
ogrenci1.numara = 123

print(ogrenci1.bilgileri_goster())


""" ogrenci1 nesnesinin özellikleri (ad, soyad, numara) sinifin disinda manuel olarak atanir. Yani, her nesne oluşturulduğunda özellikler elle girilmelidir.

__init__ metodu, nesne oluşturulurken otomatik olarak cagrildiginda için, her nesneye değer atamak daha kolay ve düzenli olur."""
