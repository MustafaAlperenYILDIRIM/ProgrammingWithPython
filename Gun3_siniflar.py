class Ogrenci:
    def __init__(self, ad, soyad, numara): #Yapıcı metot
        self.ad = ad
        self.soyad = soyad
        self.numara = numara

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Soyad: {self.soyad}, Numara: {self.numara}"
    
    


ogrenci1 = Ogrenci("Ahmet", "Yılmaz", 123)
print(ogrenci1.bilgileri_goster())  