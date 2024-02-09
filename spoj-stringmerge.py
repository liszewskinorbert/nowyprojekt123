wielkoscTablicy = int(input())
tablica = []
zmienna = ""
najkrotszeWyrazy = []
wynikowyCiag = []


def zlaczCiagLiter(pierwszyWyraz, drugiWyraz, iloscLiter):
    wyrazWynikowy = ""
    for i in range(0, iloscLiter):
        wyrazWynikowy += pierwszyWyraz[i]+drugiWyraz[i]
    return wyrazWynikowy


for i in range(0, wielkoscTablicy):
    zmienna = input().split()
    #print(len(zmienna))
    tablica.append(zmienna[0])
    if len(zmienna) > 1 :
        tablica.append(zmienna[1])
    else:
        tablica.append("")


for i in range(0, wielkoscTablicy):
    if len(tablica[i*2]) <= len(tablica[i*2+1]):
        najkrotszeWyrazy.append(len(tablica[i*2]))
    elif len(tablica[i*2]) > len(tablica[i*2+1]):
        najkrotszeWyrazy.append(len(tablica[i*2+1]))


for i in range (0, len(najkrotszeWyrazy)):
    wynik = zlaczCiagLiter(tablica[i*2], tablica[i*2+1], najkrotszeWyrazy[i])
    print(wynik)




