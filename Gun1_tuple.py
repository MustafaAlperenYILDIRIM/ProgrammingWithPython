"""#tuple
tuple1=(1,2,"tuple",10,15)
tuple2=()
tuple3=tuple((1,10,100,"Ankara"))

print(tuple1)
print(tuple2)
print(tuple3)

print(tuple3[3])"""


tuple_example=(1,2,3,4,56,76,23,"Python Eğitimi")
print(tuple_example)

print(tuple_example.index(56))
print((tuple_example[-1]))# -1 sondan bir önceki elemanı verir
print(tuple_example[1:6])#1. elemandan 6. elemana kadar olan elemanları verir
print(len(tuple_example))


#tuple_example[0]=5 #tuple elemanları değiştirilemez

aylar=("Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık")
print(type(aylar))
print(aylar)

liste_aylar=list(aylar)
print(type(liste_aylar))
print(liste_aylar)

"""a=7
b=str(a)"""