class InternetHizmeti:
    def __init__(self, hiz, fiyat, servis_turu):
        self.hiz = hiz           
        self.fiyat = fiyat       
        self.servis_turu = servis_turu  

    def hizmet_bilgisi(self):
        return f"İnternet Hizmeti: {self.servis_turu}, Hız: {self.hiz} Mbps, Fiyat: {self.fiyat} TL"

    def hizmet_detaylari(self):
        raise NotImplementedError("Bu metod alt sınıf tarafından özelleştirilmelidir.")

class TurkTelekomHizmeti(InternetHizmeti):
    def __init__(self, hiz, fiyat, servis_turu, yonetim_ekipman):
        super().__init__(hiz, fiyat, servis_turu)  
        self.yonetim_ekipman = yonetim_ekipman    

    def hizmet_detaylari(self):
        return f"{self.hizmet_bilgisi()} - Yönetim Ekipmanı: {self.yonetim_ekipman}"

class FiberOptikHizmeti(TurkTelekomHizmeti):
    def __init__(self, hiz, fiyat, servis_turu, yonetim_ekipman, fiber_tekniği):
        super().__init__(hiz, fiyat, servis_turu,yonetim_ekipman)  
        self.fiber_tekniği = fiber_tekniği        

    def hizmet_detaylari(self):
        return f"{self.hizmet_bilgisi()} Yönetim Ekipmanı: {self.yonetim_ekipman} - Fiber Teknolojisi: {self.fiber_tekniği}"
#BİTİŞ-9:35
turk_telekom = TurkTelekomHizmeti(100, 500, "VDSL", "Modem")
fiber_internet = FiberOptikHizmeti(1000, 700, "Fiber", "ONT","GPON")
internet=InternetHizmeti(16,300,"ADSL")
print(internet.hizmet_bilgisi())
print(turk_telekom.hizmet_detaylari()) 
print(fiber_internet.hizmet_detaylari())  

#MİRAS ALINACAK CLASS'I OLUŞTURALIM
#ALTINA 2 ADET CLASS OLUŞTURUP , ÜST SINIFTAN YAPICI METOT VE BİR FONKSİYONUNU MİRAS ALSINLAR
#ANA SINIF: ÇALIŞAN ADINDA BİR SINIF; AD,SOYAD,MAAŞ GİBİ TEMEL ÖZELLİKLERİ TANIMLAYALIM
#ALT SINIF-1: KENDİ ÜNVANINIZLA BİR SINIF OLUŞTURUN, İŞİNİZ İLE ALAKALI BİR ÖZELLİK EKSTRADAN-
#-EKLEYELİM(KULLANDIĞI PROGRAM BİLGİSİ)
#ALT SINIF-2: BENZER FARKLI BİR ÜNVAN(YÖNETİCİ) BELİRLEYİP ALT SINIF-1'DEN KALITIM YOLUYLA ÖZELLİK ALARAK EKSTRA OLARAK
#-BİR ÖZELLİK EKLEYELİM
#DAHA SONRASINDA PRINT METODU İLE ÖZELLİKLERİ YAZDIRALIM

#BİTİŞ: 9.35
