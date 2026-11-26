print("Hello")
from datetime import datetime, date, timedelta
# import cowsay
# cowsay.cow("woof woof")
# cowsay.dragon("miau miau")
# print(cowsay.char_names)
# cowsay.turtle("wonsz rzeczny tududu")
# print("tekst", "inny tekst")
# print("-" * 120)
# print("tekst" + " inny tekst")

# zmienne
# print("-" * 120)
# x = 5
# y = 10
# z=x+y
# print(z)
# abc=None
# print(abc)
# wartosc=123
# print(wartosc)

# print("-" * 120)
# x, y, z = 2, "Ala", 5
# print(x, y, z)
# print("-" * 120)
# x = "Ala ma kota"  # str
# y = 12  # int
# z = 12.43  # float
# q = 0.3  # 30%
# w = True

# print("-" * 120)
# y="10.44"
# xx=float(y)+z
# print(xx)
# print("-" * 120)

# wynik=16.48-16.71
# print(wynik)
# print(f"{wynik:.2f}")

# wakacje = "Łeba"
# kiedy=15
# kasa=12871634531.12345678
# #¯\_(ツ)_/¯
# print("na wakacje pojadę:", kiedy, "do miasta:", wakacje,sep="*****")
# print(f"na wakacje pojadę: {kiedy} do miasta: {wakacje} wydam: {kasa:_.2f}")
# ladna_liczba=f"{kasa:_.2f}".replace("_"," ")
# print(f"Liczba: {ladna_liczba}")
# print("-" * 120)
# print(3**3) #operator potegowania
# print(len(ladna_liczba))
# print("-" * 120)
# b = "Hello, World!"
# print(b[2:6])
# # reverse
# txt = b
# print(b[::-1])

# imie = "hubert"
# poprawione_imie = imie.upper()
# print(poprawione_imie)
# imie = imie.title()
# print(imie)
# imie=imie.title(). \
#     replace("ert","son") #backslash kontynuuje linijke w kolejnej
# print(imie)

print("-" * 120)
tekst_CSV="03/22/2025 jan KOWalski wypłata PLN: 8359"
print("rok:",tekst_CSV[6:10],"miesiac:",tekst_CSV[3:5],"dzien:",tekst_CSV[0:2])
imie_nazwisko=tekst_CSV[11:tekst_CSV.find(" wypłata")].title()
print(imie_nazwisko)
Euro_wyplata=float(tekst_CSV[tekst_CSV.find("PLN")+5:])/4.33
print(f"{Euro_wyplata:.2f}")
data = tekst_CSV[0:10]
data_corr=datetime.strptime(data,"%m/%d/%Y")
print(data_corr.date())

# #dzialanie funkcji replace musi byc przypisane do definicji zmiennej bo teksty są niezmienialne
# tekst_CSV=tekst_CSV.replace("jan KOWalski","marek pięKNy")
# tekst_CSV=tekst_CSV.replace("8359","10999.76")
# imie_nazwisko=tekst_CSV[11:tekst_CSV.find(" wypłata")].title()
# print(imie_nazwisko)
# Euro_wyplata=float(tekst_CSV[tekst_CSV.find("PLN")+5:])/4.33
# print(f"{Euro_wyplata:.2f}")


print("-" * 120)
teraz=datetime.now()
ladna_data=teraz.strftime("%d.%m.%Y. %H:%M:%S")
print(f"Teraz jest: {teraz}")
print(f"Ladna data: {ladna_data}")
urodziny=date(1995,10,25)
print(f"Urodziny: {urodziny}")
przyszlosc=teraz+timedelta(days=100)
print(f"Za 100 dni będzie: {przyszlosc.date()}")