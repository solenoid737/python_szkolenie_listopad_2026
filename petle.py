# cars = ['audi','bmw','skoda','kia']

# for pojazd in cars:
#     if pojazd=="audi":
#         print(f"Samochód: {pojazd}, kupię")
#     else:
#         print(f"Samochód: {pojazd}, - nie kupię")

# # alternatywa
# for nr in range(len(cars)):
#     if cars[nr]=="audi":
#         print(f"Samochód: {cars[nr]}, kupię")
#     else:
#         print(f"Samochód: {cars[nr]}, - nie kupię")

# garaz ={
#     "Toyota": "Corolla",
#     "Mazda": "CX-5",
#     "BMW": "M3",
#     "Tesla": "Model S"
#     }
# for marka, model in garaz.items():
#     print(f"Marka: {marka} | Model: {model}")
# # for marka
# for model in garaz.values():
#     print(f"Mam w garażu pojazd: {model}")

# przyklad
# auta_szczegoly = {
#     "WA12345": {"marka": "Toyota", "rok": 2020, "przebieg": 50000},
#     "KR67890": {"marka": "BMW", "rok": 2018, "przebieg": 120000},
# }
# for tab_rej,parametry in auta_szczegoly.items():
#     przebieg=parametry["przebieg"]
#     print(f"tab_rej: {tab_rej}, przebieg: {przebieg}")

# #alternatywa
# import dane_pojazdy
# for tab_rej,parametry in dane_pojazdy.auta_szczegoly.items():
#     przebieg=parametry["przebieg"]
#     print(f"tab_rej: {tab_rej}, przebieg: {przebieg}")
# from dane_pojazdy import auta_szczegoly as asc
# for tab_rej,parametry in asc.items():
#     przebieg=parametry["przebieg"]
#     print(f"tab_rej: {tab_rej}, przebieg: {przebieg}")

#garaz json
from garaz_dane import garaz
from prettytable import PrettyTable as pt
tabela=pt(["marka","rok","napęd"])
for marka,param in garaz.items():
    rok=param[1][0]
    naped=param[1][1]
    # print(f"marka: {marka}, rok produkcji: {rok}, naped: {naped}")
    tabela.add_row([marka,rok,naped])
print(tabela)
csv=tabela.get_csv_string()
# print(csv)