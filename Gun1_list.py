"""#list
list_1=[1,2,3,"Python","Eğitimi",4,"TürkTelekom"]
list_2=[]
list_3=list((8,1,14,2,50,150))

list_4=["Arzu","Süleyman","Eyüp"]


print(list_1)
print(list_2)
print(list_3)
print("liste 4:",list_4)

#7. elemanı yazdırma
print(list_1[6])
print(list_4[0])


#eleman ekleme - append
list_1.append("yeni nesne eklendi")
print(list_1)
list_4.append("Ziya")
print(list_4)

#eleman silme
list_1.pop(2)
print(list_1)
list_4.pop(3)
print(list_4)

#liste sıralama
list_3.sort(reverse=True)
print(list_3)

#elemanın sırasını bulma
print(list_1.index("TürkTelekom"))
a=list_4.index("Süleyman")
print(a)"""
#metotlar

list_example=[1,2,3,4,5,6,7,8,9,10] #liste oluşturma1
print(list_example)

list_example.append(11) #eleman ekleme
print(list_example)


a=list_example.pop() #eleman silme
print(a)

list_example.sort(reverse=True) #sıralama
print(list_example)

print(list_example.index(5)) #elemanın sırasını bulma
print("elaman sayısı:",len(list_example)) #liste uzunluğu

list_example[0]=5 #eleman değiştirme
print(list_example)

list_example=[1,2,3,4,5,6,7,8,9,10,5,5]
print(list_example.count(5)) #eleman sayısı