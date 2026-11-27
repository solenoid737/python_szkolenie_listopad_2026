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
marka = df["Marka"].astype("string")
marka = marka.str.strip()
marka = marka.str.upper()
# marka = marka.replace({"bmw": "BMW"})
df["Marka_clean"] = marka

kolumny = ["Kolor", "Cena_PLN", "Marka", "Marka_clean", "Data produkcji"]
filtr = ((df["Kolor"] == "Czerwony") | (df["Kolor"] == "Biały")) & (
    df["Cena_PLN"] <= 50000
)

filtr2 = (
    df["Kolor"].isin(["Czerwony", "Biały", "Różowy"])
    & (df["Cena_PLN"] <= 100000)
    & (df["Marka"].str.contains("bmw", case=False))
)
df_filtr = df.loc[filtr, kolumny].sort_values(["Cena_PLN"])
print(df_filtr)

wynik = df[df.isna().any(axis=1)]
print(wynik)

df["Cena_brutto"] = df["Cena_PLN"] * 1.23
print(df)

df["Marka_Model"] = df["Marka"].astype("string") + " " + df["Model"]
print(df)

df.loc[df["Kolor"].isin(["Czerwony", "Biały"]), "Kategoria_Koloru"] = "ładny"
df.loc[~df["Kolor"].isin(["Czerwony", "Biały"]), "Kategoria_Koloru"] = "brzydki"
df.loc[df["Cena_brutto"] < 100000, "Kategoria_Ceny"] = "drogi"
df.loc[
    (df["Cena_brutto"] >= 100000) & (df["Cena_brutto"] < 150000), "Kategoria_Ceny"
] = "bardzo drogi"
df.loc[df["Cena_brutto"] >= 150000, "Kategoria_Ceny"] = "za drogi"


print(df[["Marka_Model", "Cena_brutto", "Kategoria_Ceny", "Kolor", "Kategoria_Koloru"]])


liczba_df = df.groupby("Marka_clean").size().sort_values(ascending=False)
print(liczba_df)

lokalizacje = df["Lokalizacja"].unique()
for lok in lokalizacje:

    ramka_filtr=df.loc[df["Lokalizacja"]==lok]

    statystyki_marek = (
        ramka_filtr.groupby("Marka", as_index=False)
        .agg(
            Liczba_ofert=("Cena_PLN", "count"),
            Suma_cen=("Cena_PLN", "sum"),
            Srednia_cena=("Cena_PLN", "mean"),
        )
        .sort_values("Liczba_ofert", ascending=False)
    )

    moja_ramka=pd.DataFrame([{
        "Marka": "TOTAL",
        "Liczba_ofert":     statystyki_marek["Liczba_ofert"].sum(),
        "Suma_cen":         statystyki_marek["Suma_cen"].sum(),
        "Srednia_cena":     statystyki_marek["Srednia_cena"].mean()
    }])

    print(moja_ramka)
    statystyki_marek=pd.concat([statystyki_marek,moja_ramka])

    print(statystyki_marek)
    statystyki_marek.to_excel("dane\\"+lok+".xlsx",index=False,sheet_name="moje_dane")

# policz ile jest pojazdów ładnych i brzydkich
# policz udział porcentowy w totalu tych danych

kolorki=(
    df.groupby("Kategoria_Koloru",as_index=False)
    .agg(
        Ile=("Cena_PLN","count"),
    ).sort_values("Ile",ascending=False)
)

total=df["Cena_PLN"].count()
kolorki["udzial %"] = (kolorki["Ile"]/total)*100

moja_ramka=pd.DataFrame([{
    "Kategoria_Koloru": "TOTAL",
    "Ile": total,
    "udzial %": 100.0
}])
wynik=pd.concat([kolorki,moja_ramka],ignore_index=True)
print(wynik)