"""lang = input("What's the programming language you want to learn? ").lower()

match lang:
    case "javascript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "php":
        print("You can become a backend developer")

    case "solidity":
        print("You can become a Blockchain developer")

    case "java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")"""

#match-case tekrar 
#aşağıdaki zar oyununu yazıp test edelim 
import random

print("Sayı tahmin oyununa hoşgeldiniz!")

zar=random.randint(1,6) #1-6 arasında rastgele bir sayı üretir

print(f"Zarın değeri: {zar}")

match zar:
    case 1:
        print("Zar 1 geldi! Şanssız bir gün olabilir.")
    case 2:
        print("Zar 2 geldi' Şansını biraz daha zorlamalısın")
    case 3:
        print("Zar 3 geldi! Daha iyi olabilir.")
    case 4:
        print("Zar 4 geldi! İyi atış!")
    case 5:
        print("Zar 5 geldi! şanslısın!")
    case 6:
        print("Zar 6 geldi! Bugün senin günün!")
    case _:
        print("Hatalı değer girişi sistemi kontrol ediniz.")
