bakiye = 0

while True:
    print("Para yatirmak icin [1], Para cekmek icin [2], Bakiyeyi sorgulamak icin [3], Cikmak icin [0]")
    islem = input("Yapmak istediginiz islemi secin.")

    try:
        islem = int(islem)
    except ValueError:
        print("Hatali giris yaptiniz. Sadece [0],[1],[2],[3] islemlerini yapabilirsiniz.")
        continue

    #para yatirma
    if islem == 1:
        x = input("Yatirmak istediginiz miktari giriniz : ")
        try:
            x = int(x)
            bakiye += x
            print("Guncel bakiyeniz: {}".format(bakiye))
        except ValueError:
            print("Lutfen sadece sayisal degerler girin.")

    #para cekme
    elif islem == 2:
        x = input("Cekmek istediginiz miktari giriniz : ")
        try:
            x = int(x)
            if x > bakiye:
                print("Bakiye yetersiz. En fazla cekilebilir miktar {}".format(bakiye))
            else:
                bakiye -= x
                print("Guncel bakiyeniz: {}".format(bakiye))
        except ValueError:
            print("Lutfen sadece sayisal degerler girin.")

    #bakiye sorgulama
    elif islem == 3:
        print("Bakiyeniz : {}".format(bakiye))

    #cikis yapma
    elif islem == 0:
        print("Cikis yapiliyor... Bizi tercih ettiginiz icin tesekkur ederiz.\n Son durum bakiyeniz {}.".format(bakiye))
        break

    else:
        print("Hatali giris yaptiniz. Boyle bir islem turu yok.")
