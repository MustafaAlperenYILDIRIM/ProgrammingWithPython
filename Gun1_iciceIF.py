#İnternet arıza senaryosu

modem=input("Modem ışıklarınız yanıyor mu? (evet/hayır):").lower()

if modem=="evet":
    internet=input("Cihaz internete bağlanıyor mu? (evet/hayır):").lower()
    if internet=="evet":
        hiz=input("İnternet hızınız düşük mü? (evet/hayır):").lower()
        if hiz=="evet":
            print("Hız kaynaklı problem. Lütfen hız testi yapınız,düşük olması durumunda 444 14 15'i arayınız.")
        else: print("İnternet bağlantınızda problem yok.")
    
    else: print("Cihaz internete bağlanmıyor. Wifi şifresini kontrol edin doğruysa modemi yeniden başlatınız.")

elif modem=="hayır":
    elektrik=input("Elektrik bağlantısını kontrol ediniz. Elektrikler var mı? (evet/hayır):").lower()
    if elektrik=="evet":
        print("Modem arızalı olabilir. Modemi yeniden başlatınız.Çözülmezse 444 14 15'i arayrak arıza kaydı oluşturunuz.")
    else: print("Elektrik bağlantısını kontrol ediniz. Telekom kaynaklı arıza yok elektrikçiye danışınız.")

elif modem=="biraz":
    print("biraz olamaz")

else:
    print("Geçerli bir değer giriniz.")

        

