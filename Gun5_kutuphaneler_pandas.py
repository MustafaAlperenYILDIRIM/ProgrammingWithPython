import pandas as pd


seri = pd.Series([10, 20, 30, 40])
print("Seri:")
print(seri)


veri = {
    "Ad": ["Ahmet", "Özden", "Emrullah"],
    "Yaş": [25, 30, 35],
    "Maaş": [3000, 4000, 5000],
}

df = pd.DataFrame(veri)
print("\nDataFrame:")
print(df)
