# listy
owoce = ["jablko", "banan", "wisnia", "banan"]
# dozwolone duplikaty

# print(owoce[0])
# print(owoce[0:])
# # Lista
# owoce.sort()
# owoce.append(["tru", "ska", "wa"])
# owoce.extend(["tru", "ska", "wa"])
# print(owoce[0])
# print(owoce[0:])

# print("-" * 120)
# owoce = [
#     ["jablko", "banan", "wisnia", "banan"],
#     ["jablko", "banan", "wisnia", "truskawa", "abc"],
# ]
# el = owoce[1][3]
# print(el)
# owoce[0][2] = "kiwi"
# print(owoce[0:])
# print(len(owoce[1]))


# tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
# moja_lista = tekst_CSV.split()
# print(moja_lista)
# # ['03/22/2025', 'jan', 'KOWalski', 'wypłata', 'PLN:', '8359']
# moja_lista.append(moja_lista[1]+" "+moja_lista[2])
# moja_lista.pop(1)
# moja_lista.pop(1)
# # alternatywa
# # del moja_lista[2:4]

# moja_lista[4]=moja_lista[4].title()

# print(moja_lista)

print("-" * 120)
# krotki - tuple
krotka = ("ala", 3, "koty")
owoce = ("jablko", "banan", "wisnia", "banan")
print(owoce)
# dzialania tutaj nie zadzialaja bo krotki sa niezmienne w przeciwienstwie do zwyklych list owoce[2]=??
punkt = (10, 20)
x, y = punkt
print(x)
print(y)

zbior={"jablko", "banan", "wisnia", "banan"}
print(zbior)
print(list(zbior))

# slowniki-dictionaries, musza byc typu niezmienialnego (unmutable)
dict={
    "brand":"BMW",
    "model":"M4 GT3",
    "year":2021,
    "driver":"Bill Auberlen",
    28:"drivers number",
    (27.0,26.7):"psi front rear",
}
print(dict)
print(dict.get("brand"),dict.get("model"),dict.get("driver"))
print(dict.items())
