tel_rehberi = dict()

def tel_no_ekle(x):
    print("***NUMARA EKLEME***")
    isim = input("isim:" )
    numara = input("numara: ")
    x = tel_rehberi.setdefault(isim, numara)
    print(f"{isim} adli kişi rehbere eklendi")

def rehber_goster(x):
    print("rehbere hosgeldiniz")

    for i,j in x.items():
        print(i, ":",j)

def no_sil(x):
    print("kisi silme ekranina hosgeldiniz")
    silinecek_isim = input("silmek istediginiz kisinin ismini giriniz: ")
    x=tel_rehberi.pop(silinecek_isim)


while True:
    print("rehber kayit sistemine hos geldiniz")
    print("1-Ekle\n2-Rehber goster\n3-Sil\n0-cikis")
    secim = int(input("secim yapiniz:"))
    if secim == 1:
        tel_no_ekle(tel_rehberi)
    elif secim == 2:
        rehber_goster(tel_rehberi)
    elif secim == 3:
        no_sil(tel_rehberi)
    elif secim == 0:
        print("cikis yapiliyor...")
        break
    else:
        print("gecerli bir sayi giriniz...")