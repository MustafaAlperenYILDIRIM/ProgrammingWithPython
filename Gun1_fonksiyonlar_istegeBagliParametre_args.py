#**kwargs (keyword arguments): genellikle daha esnek ve dinamik parametreler alabilen fonksiyonlar oluşturmak için kullanılır.

def istegeBagliParametre(**Parametreler):
    for deger in Parametreler.items():
        print(f"{deger[0]} : {deger[1]}")

istegeBagliParametre(ilkParametre="Canın",ikinciParametre="İstediği",ucuncuParametre="Gibi",dorduncuParametre="Kullan")


#**kwargs (keyword arguments): genellikle daha esnek ve dinamik parametreler alabilen fonksiyonlar oluşturmak için kullanılır.

def a(*x):
    for deger in x:
        print(deger)

a()
