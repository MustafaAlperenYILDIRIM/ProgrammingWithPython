def islem(*args):
   
    if len(args) == 1:  
        if isinstance(args[0], int):  
            return f"Karesi: {args[0] ** 2}"
        elif isinstance(args[0], str):  
            return f"Büyük harf: {args[0].upper()}"
        elif isinstance(args[0], list):  
            return f"Liste eleman sayısı: {len(args[0])}"
        else:  
            return "Bu tür desteklenmiyor!"
    
    elif len(args) == 2:  
        return f"Toplam: {args[0] + args[1]}"
    
    else:  
        return "Bu islem desteklenmiyor!"


print(islem(4))            
print(islem("Merhaba"))    
print(islem([1, 2, 3, 4])) 
print(islem(5, 10))        
#print(islem(5, "abc"))     
print(islem())             
