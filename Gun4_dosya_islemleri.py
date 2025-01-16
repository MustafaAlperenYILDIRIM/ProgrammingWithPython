dosya = open("dosya.txt", "w")

dosya.write("20.12.2024 Günlük Notlar\n")

dosya.close()

dosya= open("dosya.txt","a")
dosya.write("Hakedişin son günü, saat 21.00 ve planlama hala çalışıyor")


dosya.close()

"""

with open(r"D:\Desktop\work\TT_internal_trainer\Codes\dosya.txt", "w") as dosya:
    dosya.write("20.12.2024 Günlük Notlar\n")


with open(r"D:\Desktop\work\TT_internal_trainer\Codes\dosya.txt", "a") as dosya:
    dosya.write("Hakedişin son günü, saat 21.00 ve planlama hala çalışıyor")
"""



