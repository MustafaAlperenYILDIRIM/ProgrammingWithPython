from functools import singledispatch

@singledispatch
def islem(param):
    return f"Desteklenmeyen tür: {type(param).__name__}"

@islem.register(int)
def _(param):
    return f"Tam sayı: {param} karesi = {param ** 2}"

@islem.register(str)
def _(param):
    return f"Metin: {param.upper()}"

@islem.register(list)
def _(param):
    return f"Liste uzunluğu: {len(param)}"


print(islem(int(input("Bir değer giriniz: "))))     
print(islem("Python"))   
print(islem([1, 2, 3]))  
print(islem(3.14))       
