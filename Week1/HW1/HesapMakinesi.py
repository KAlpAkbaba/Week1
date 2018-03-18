while True:
    s1 = int(input("1. Sayiyi Giriniz : "))
    s2 = int(input("2. Sayiyi Giriniz : "))
    print("")
    print("---------------------------------")
    print("-- Toplama Islemi Icin (+) --")
    print("-- Cikarma Islemi Icin (-) --")
    print("-- Carpma Islemi Icin (*) --")
    print("-- Bolme Islemi Icin (/) --")
    print("---------------------------------")
    print("")
    islem = str(input("Yapilacak Islemi Giriniz : "))
    if islem == "+":
        snc = s1 + s2
        print("Cevabınız :", snc)
    elif islem == "-":
        snc = s1 - s2
        print("Cevabınız :", snc)
    elif islem == "*":
        snc = s1 * s2
        print("Cevabınız :", snc)
    elif islem == "/":
        if s1 == 0 or s2 == 0:
            print("")
            print("0 a rakam bölünmez")
        if s2 > s1.
            print("")
            print("İkinci Sayı Birinci Sayıdan Büyük Olduğu İçin Bölme İşlemi Yapılamaz.")
        if s1 == 0 and s2 > s1
            print("")
            print("0 'a Sayı Bölünmez")
        elif s1 != 0 or s2 != 0:
            snc = s1 / s2
            print("Cevabınız :", snc)

    elif islem == "exit":
        exit()
    else:
        print("Islem Harfi Gecersiz ...")
