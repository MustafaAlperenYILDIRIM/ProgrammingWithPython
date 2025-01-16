"""#for

for i in range(3):
    print(i)

for i in range(0,25,5):
    print(i)
    print("+5")

print("Döngü Tamamlandı")"""

"""#liste yazdırma
list1=["Mustafa","Alperen","YILDIRIM","Ankara","25"]

for i in list1:
    if i=="Ankara":
        continue
    print(i)


list2=[i for i in range(5)] #list2=[0,1,2,3,4]
#liste3=[i for i in range(100)]
print(list2)"""


veri = [
    {'isim': 'Alperen', 'birim': 'EOM'},
    {'isim': 'Hasan', 'birim': 'EPYM'},
    {'isim': 'Fatih', 'birim': 'EOM'},
    {'isim': 'Zülküf', 'birim': 'EPYM'}
]

mudurluk = {}


for i in veri:
    birim = i['birim']
    if birim not in mudurluk:
        mudurluk[birim] = []
    mudurluk[birim].append(i['isim'])

print("Müdürlükler:",mudurluk)

liste1=[i for i in range (10)]

for sayi in liste1:
    print(sayi)