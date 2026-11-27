import pandas as pd

# Odczyt pliku
df = pd.read_excel(r"dane\samochody.xlsx", sheet_name="dane")

# print(df.head())
# print(df.shape)

df2 = pd.read_csv(r"dane\dane.csv")
# print(df2.head())
# print(df2.shape)

# print(df.columns.tolist())
# print(df.dtypes)

# drogie_pojazdy = df[df["Cena_PLN"] > 140000]
# print (drogie_pojazdy.to_string())

kolumny = ["Kolor", "Cena_PLN", "Marka", "Data produkcji"]
filtr = ((df["Kolor"] == "Czerwony") | (df["Kolor"] == "Biały")) & (
    df["Cena_PLN"] <= 50000
)
filtr2 = (
    df["Kolor"].isin(["Czerwony", "Biały", "Różowy"])
    & (df["Cena_PLN"] <= 100000)
    & (df["Marka"].str.contains("bmw",case=False))
)
df_filtr = df.loc[filtr2, kolumny].sort_values(['Cena_PLN'])
print(df_filtr)

wynik = df[df.isna().any(axis=1)]
print(wynik)

df["Cena_brutto"]=df["Cena_PLN"]*1.23
print(df)