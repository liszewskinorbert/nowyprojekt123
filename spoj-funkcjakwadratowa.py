
while 1:
    try:
        a, b, c = input().split()
        delta = float(b) * float(b) - 4 * float(a) * float(c)

        if delta < 0:
             print("0")
        elif delta == 0:
             print("1")
        else:
             print("2")
    except:
        break



