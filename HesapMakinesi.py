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
islem=str(input("Yapilacak Islemi Giriniz : "))
if islem =="+":
    snc=s1+s2
    print("Cevabınız :",snc)
elif islem =="-":
    snc=s1-s2
    print("Cevabınız :",snc)
elif islem =="*":
    snc=s1*s2
    print("Cevabınız :",snc)
elif islem =="/":
    snc=s1/s2
    print("Cevabınız :",snc)
else :
    print("Islem Harfi Gecersiz ...")
