from functools import singledispatchmethod

class islem:
    @singledispatchmethod
    def hesapla(self, param):
        return f"Desteklenmeyen tür: {type(param).__name__}"

    @hesapla.register
    def _(self, param: int):
        return f"Tam sayı karesi: {param ** 2}"

    @hesapla.register
    def _(self, param: str):
        return f"Büyük harf: {param.upper()}"

    @hesapla.register
    def _(self, param: list):
        return f"Liste uzunluğu: {len(param)}"


islem1 = islem()
print(islem1.hesapla(5))            
print(islem1.hesapla("python"))     
print(islem1.hesapla([1, 2, 3]))    
print(islem1.hesapla(3.14))         


"""
class İşlem:
    def __call__(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            return f"Tam sayı karesi: {args[0] ** 2}"
        elif len(args) == 2:
            return f"İki sayının toplamı: {args[0] + args[1]}"
        else:
            return "Desteklenmeyen islem1!"

# Kullanım
islem1 = İşlem()
print(islem1(4))        # Tam sayı karesi: 16
print(islem1(3, 7))     # İki sayının toplamı: 10
print(islem1("test"))   # Desteklenmeyen islem1!
"""