kelime = input("Bir kelime girin : ")
a = []
b = []
for i in kelime:
    a.append(i)
uzunluk = len(kelime)

for x in range(0, uzunluk):
    a.append(a[x])

print('\n\n')
i = uzunluk
i = i - 1
while (i >= 0):
    b.append(a[i])
    i = i - 1
sayac = 0
for xx in range(0, uzunluk):
    if a[xx] == b[xx]:
        sayac = sayac + 1

if sayac == uzunluk:
    print("Girilen string Palindrome' dur.")
else:
    print("Girilen string Palindrome degildir.")
