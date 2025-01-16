dict1={"TT":"Türk Telekom","CBS":"Coğrafi Bilgi Sistemi","Kaşif":"Proje Çizim Uygulaması"}

print("\n", dict1.keys())
print(dict1.values())
print(dict1['TT'])
print(dict1, "\n")

#bilgi ekleme
dict1.update({"Prizma":"Rapor Bilgi Sistemi"})
print(dict1, "\n")

#bilgi silme
dict1.pop("Kaşif")
print(dict1,"\n")


"""veri = [
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

print("Müdürlükler:",mudurluk)"""

