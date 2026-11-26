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