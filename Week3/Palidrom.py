a = str(input("Kelime Girin :"))
b = len(a)
c = True
if b % 2 == 0:
    print("Palidrom Değildir...")
else:
    ord = round(b / 2)
    for i in range(0, ord):
        if a[i] != a[0 - (i + 1)]:
            print("Palidrom Değildir...")
            c=False
            break
    if c:
        print("Palidromdur.")
