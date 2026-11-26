# bloki warunkowe
kolor = "rozowy"

if kolor=="bialy":
    print("kupię")
elif kolor == "rozowy":
    print("SUPER!")
else:
    print("nie kupię")
print("test")

kolor = "zielony"
cena=90000
# kupie zielony w cenie do 65k biały

if (kolor=="zielony" or\
    kolor=="biały") and\
    cena<=65000:
    print("kupię")

#####################################################
# pobranie od usera
from tkinter import simpledialog

cena = input("Podaj cenę: ")
test = "343"
print(test.isdigit())
if cena == "":
    print("brak ceny")
elif cena.isdigit() == False:
# elif not cena.isdigit(): - bardziej elegancka alternatywa
    print("Podaj liczbe!")
else:
    print(f"cena: {cena}")

kurs = simpledialog.askfloat("Waluta","Podaj kurs",
                             minvalue=1.0, maxvalue=10.0,
                             initialvalue=5.0)
if kurs == None:
    print("nie podano kursu")
    exit()
print(f"{float(cena)/kurs:.2f}")

# przyklad
