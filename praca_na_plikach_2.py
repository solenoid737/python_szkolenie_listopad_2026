# import samochody z pliku dane.csv
from prettytable import PrettyTable as pt
import time

max_wiersz=2e6
suma_total=0
ile_total=0
ile = 0
pojazdy={} #tworzymy pusty slownik

czas_start = time.time()
with open(r"dane\dane_2_mln.csv", encoding="utf-8") as plik:
    for wiersz in plik:
        if ile == 0:
             ile+=1
             continue
        else:
        #      print(wiersz.strip())
        #      ile = ile + 1
             ile += 1
             if ile == max_wiersz:
                 break
             lista=wiersz.split(";")
             marka = lista[1]
             cena=float(lista[2])
             suma_total+=cena
             ile_total+=1

             lokalizacja = lista[7]
             if lokalizacja not in pojazdy:
                 pojazdy[lokalizacja]={}

             if marka not in pojazdy[lokalizacja]:
                 pojazdy[lokalizacja][marka]=[0,0]

             cena_obl=pojazdy[lokalizacja][marka][0]+cena
             liczba_obl=pojazdy[lokalizacja][marka][1]+1
             pojazdy[lokalizacja][marka]=[cena_obl,liczba_obl]

# print(f"pojazdow jest: {ile_total}, cena razem: {suma_total}")
# print(pojazdy)

tab=pt(["pojazd","cena","ilość","średnia"])

for lokalizacja,x in pojazdy.items():

    tab=pt(["pojazd","cena","ilość","średnia"])
    
    for marka, y in x.items():
        ceny=f"{y[0]:_.0f}".replace("_"," ")
        ile=y[1]
        cena_avg=f"{y[0]/ile:_.0f}".replace("_"," ")
        #     cena_avg=round(y[0]/y[1],1)
        tab.add_row([marka,ceny,ile,cena_avg])
# print(tab)

    with open("dane\\"+lokalizacja+".txt","w",encoding="utf-8",newline="") as plik:
        plik.write(tab.get_string())
        plik.write("\n\n")
        plik.write(tab.get_csv_string(delimiter=";"))

czas_koniec = time.time()

ile_trwalo=f"{czas_koniec-czas_start:.2f} s"
print(f"czas: {ile_trwalo}")