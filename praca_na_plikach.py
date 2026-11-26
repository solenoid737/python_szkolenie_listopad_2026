plik = open(r"dane\moje_dane.txt", "rt")
zaw = plik.read()
plik.close()\

#alternatywa

with open(r"dane\moje_dane.txt","rt") as plik:
          zaw = plik.read()

print(zaw)
with open(r"dane\moje_dane.txt","a") as plik:
        plik.write("\nnowa zawartosc")