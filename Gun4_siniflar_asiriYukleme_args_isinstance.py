class islem:
    def hesapla(self, *args):
        if len(args) == 1 and isinstance(args[0], int):  
            return f"Tam sayı karesi: {args[0] ** 2}"
        
        elif len(args) == 2 and all(isinstance(x, int) for x in args):  
            return f"İki sayının toplamı: {args[0] + args[1]}"
        
        elif len(args) == 1 and isinstance(args[0], str):  
            return f"Büyük harf: {args[0].upper()}"
        
        else:
            return "Desteklenmeyen islem1!"


islem1 = islem()
print(islem1.hesapla(5))          
print(islem1.hesapla(3, 7))       
print(islem1.hesapla("python"))   
print(islem1.hesapla(3.14))       
