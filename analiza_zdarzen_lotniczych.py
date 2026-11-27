from dane.dane_zdarzenia import zdarzenia as zd
from tkinter import simpledialog
from prettytable import PrettyTable as pt

wybor = simpledialog.askstring(
    "Format raportu", "W jakim formacie zapisać wynik? Wpisz: csv lub json"
)

if wybor is None:
    print("Anulowano przez użytkownika. Koniec programu.")
    exit()

wybor = wybor.strip().lower()

if wybor != "csv" and wybor != "json":
    print(f"Błędny format: '{wybor}'. Dozwolone: csv lub json.")
    exit()


ile_total = 0
ile_minor = 0
ile_serious = 0
po_lotnisku = {}
po_typie = {}

for data, icao, typ, powaga, samolot in zd:
    ile_total = 1
    if powaga == "serious":
        ile_serious += 1
    else:
        ile_minor += 1
    if icao not in po_lotnisku:
        po_lotnisku[icao] = [0, 0]
    # print(po_lotnisku)
    # exit()

    po_lotnisku[icao][0] += 1
    if powaga == "serious":
        po_lotnisku[icao][1] += 1

    if typ not in po_typie:
        po_typie[typ] = 0
    po_typie[typ] += 1
    # print(po_typie)
    # exit()

tab_lotniska = pt(["Lotnisko", "Razem", "Minor", "Serious", "Ryzyko (%)"])
lotniska_do_json = {}
for icao, dane in po_lotnisku.items():
    razem = dane[0]
    serious = dane[1]
    minor = razem - serious
    ryzyko = round((serious / razem) * 100, 1)

    tab_lotniska.add_row([icao, razem, minor, serious, f"{ryzyko}%"])

print("\n=== ANALIZA PO LOTNISKU (ICAO) ===")
print(tab_lotniska)

tab_typy = pt(["Typy zdarzenia", "Liczba"])

for typ, liczba in po_typie.items():
    tab_typy.add_row([typ, liczba])

print("\n=== ANALIZA PO TYPIE ZDARZENIA ===")
print(tab_typy)

if wybor == "csv":
    sciezka = r"dane\raport_lotniczy.csv"
    with open(sciezka, "w", encoding="utf-8", newline="") as plik:
        plik.write(tab_lotniska.get_csv_string(delimiter=";"))
        plik.write("\n")
        plik.write(tab_typy.get_csv_string(delimiter=";"))
    print(f"\nZapisano raport CSV do pliku: {sciezka}")

elif wybor =="json":
    sciezka = r"dane\raport_lotniczy.json"
    with open(sciezka, "w", encoding="utf-8") as plik:
        plik.write(tab_lotniska.get_json_string())
        plik.write(tab_typy.get_json_string())
    print(f"\nZapisano raport JSON do pliku: {sciezka}")