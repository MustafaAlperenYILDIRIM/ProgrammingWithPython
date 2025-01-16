import seaborn as sns
import matplotlib.pyplot as plt


# Basit bir çizgi grafiği
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Basit Çizgi Grafiği")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.show()



# Basit bir kutu grafiği
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Günlere Göre Hesap Dağılımı")
plt.show()
print(tips.head())

