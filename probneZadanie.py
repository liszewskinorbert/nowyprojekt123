wynik = 0
while 1:

    try:
        linia = input()
        if linia != "":
            wynik += int(linia)
        else:
            break
    except:
        break

print(wynik)