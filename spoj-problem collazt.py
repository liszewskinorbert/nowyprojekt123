def collatz(number):
    number = int(number)
    lst = []
    lst.append(number)
    while (number != 1):
        if (number % 2 == 0):
            number = number // 2
            lst.append(number)
        else:
            number = number * 3 + 1
            lst.append(number)
    print(len(lst)-1)




wielkoscTablicy = int(input())
tablica = []



for i in range(0,wielkoscTablicy):
    tablica.append(input())


print(tablica)

for element in tablica:
    collatz(element)

