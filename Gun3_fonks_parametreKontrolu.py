def islem(*args):
    if len(args) == 1:
        return args[0]**2 #karesini al
    
    elif len(args)>=2:
        return args[0]+args[1] # iki sayıyı topla
    
    else:
        return "en fazla 2 eleman için tasarlanmıştır."

print("Karesini almak istediğiniz sayıyı veya toplamak istediğiniz iki sayıyı giriniz:")
print(islem(4))#kare aldık
print(islem(4,5))#toplama yaptık
print(islem(4,5,6,7))

