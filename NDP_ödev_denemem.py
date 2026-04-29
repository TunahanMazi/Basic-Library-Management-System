#------------------------------------------
#--------KÜTÜPHANE YÖNETİM SİSTEMİ---------
#------------------------------------------
#-----------ESENLİKLER DİLERİM-------------
#------------------------------------------
"""
-------------------------------------------------
----------- KÜTÜPHANE YÖNETİM SİSTEMİ -----------
-----------------------------------------*
--------
"""
def ana_menu(): #Anamenü fonksiyonu
    while True:
        print("Kütüphane Yönetim Sistemine Hoşgeldiniz.",
              "\n 1. Kitap Ekle",
              "\n 2. Kitap Ara",
              "\n 3. Çıkış")
        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz: (1-3)").strip()

        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitap_ara()
        elif secim == "3":
            print("Programdan Çıkılıyor...")
            break
        else:
            print("Sadece 1-3 arasında bir sayı giriniz")
#-------------------------------------------------------------------------
def kitap_ekle(): #Kitap ekleme fonksiyonu
    print("------KİTAP EKLEME MODÜLÜ------"
          "\n Lütfen 25 adet kitap giriniz.")
    eklenen_kitap_sayisi = 0
    while eklenen_kitap_sayisi <25:
        print(f"\n--- Yeni Kitap Kaydı ({eklenen_kitap_sayisi + 1}/25) ---")
        
        while True:
            kitap_ismi = input("Kitap adı giriniz: ").strip().lower()
            if len(kitap_ismi) > 0:
                kitap_ismi_var_mi = False
                try: # Dosyayı okuma modunda
                    dosya = open("kitaplar.txt", "r", encoding="utf-8")
                    for satir in dosya:
                        kayit = satir.strip().split("|")
                        if len(kayit) >= 1 and kayit[0] == kitap_ismi:
                            kitap_ismi_var_mi = True
                            break
                    dosya.close()
                    
                except FileNotFoundError:
                    pass
                if kitap_ismi_var_mi:
                    print("Varolan bir kitap adı girilemez!")
                else:
                    break
            else:
                print("Hata! Kitap adı boş bırakılamaz.")
                
        while True:
            kitabin_yazari = input("Kitabın yazarını giriniz: ").strip().lower()
            if len(kitabin_yazari) > 0: #isalpha kullanırsak "Ahmet Ümit" yazamaz ama özel değerler girebilir. Bu bizi aşar.
                break
            else:
                print("Hatalı Giriş Yaptınız.")
                
        while True:
            isbn_no = input("isbn: (Örn: 978-975-01-01)")
            if isbn_no.replace("-","").isdigit():
                if len(isbn_no.replace("-", "")) == 10:
                    isbn_var_mi = False
                    try: # Dosyayı okuma modunda açıyoruz
                        dosya = open("kitaplar.txt", "r", encoding="utf-8")
                        for satir in dosya:
                            kayit = satir.strip().split("|")
                            # Dosyadaki verileri parçalayıp 3. sıradaki (index 2) ISBN'ye bakıyoruz
                            if len(kayit) >= 3 and kayit[2] == isbn_no:
                                isbn_var_mi = True
                                break # Eşleşme bulursak aramayı durduruyoruz
                        dosya.close()
                    except FileNotFoundError:
                        pass
                    if isbn_var_mi:
                        print("Varolan bir ISBN numarası girilemez!")
                    else:
                        break
                else:
                    print("Hata! ISBN numarası 10 rakam içermeli.")
            else:
                print("Hatalı Giriş Yaptınız.")
        
        while True:
            yayin_yeri = input("Yayın yeri giriniz: ").strip().lower()
            if yayin_yeri.replace(" ","").isalpha():
                break
            else:
                print("Hatalı Giriş Yaptınız.")

#-------------------TXT DOSYASINA YAZDIRMA YERİ-------------------------
#-----------------------------------------------------------------------
        try:
            dosya = open("kitaplar.txt", "a", encoding="utf-8")
            dosya.write(f"{kitap_ismi}|{kitabin_yazari}|{isbn_no}|{yayin_yeri}\n")
            dosya.close()
            print(f"\nGirdiğiniz '{kitap_ismi.capitalize()}' kitabı veri tabanına başarıyla yazdırıldı.")
            eklenen_kitap_sayisi += 1

        except:
            print("Hata! Veri, dosyaya yazılamadı.")
        if eklenen_kitap_sayisi == 25:
            print("\nTebrikler! 25 adet kitap başarıyla eklendi. Ana menüye dönülüyor.")
            return
#------------------------------------------------------------------------------------------------------------------
        while True:
            secim0 = input("\nYeniden ekleme yapmak için 0'ı, Anamenüye dönmek için 1'i tuşlayınız.") #ya da int(input())
            if secim0 == "0":
                break #break diyerek bir önceki tab (for) döngüsüne geri alıyor.
            elif secim0 == "1":
                return
            else:
                print("Lütfen sadece 0 veya 1 tuşuna basınız.")
                continue
#------------------------------------------------------------------------------------------------------------------
def kitap_ara(): #Kitap arama fonksiyonu
    print("------KİTAP ARAMA MODÜLÜ------")
    while True:
        print("Nasıl bir arama yapmak istersiniz?"
        "\n,",
        "\n 1. İçinde geçen metne göre arama (Örn: 'Emr' içeren)",
        "\n 2. ISBN numarasına göre arama (Örn: '978-975-01-01' ile başlayan)",
        "\n 3. Yazarına göre arama (Örn: Orwell)",
        "\n 4. Ana menüye dön")

        secim1 = input("Lütfen yapmak istediğiniz işlemi seçiniz: (1-4)").strip()
        if secim1 == "4":
            print("Ana menüye dönülüyor...")
            break
        elif secim1 != "1" and secim1 != "2" and secim1 != "3":
            print("Sadece 1-4 arasında bir sayı giriniz")
            continue
        aranan_kelime = input("Aranacak metni giriniz.").strip().lower()

        eslesen_kitaplar = []
        try:
            dosya = open("kitaplar.txt", "r", encoding="utf-8")
            for satir in dosya:
                satir = satir.split("|")
                if(aranan_kelime in satir[0].lower().strip() or
                   aranan_kelime in satir[1].lower().strip() or
                   aranan_kelime in satir[2].lower().strip() or
                   aranan_kelime in satir[3].lower().strip()):
                    eslesen_kitaplar.append(satir)
            dosya.close()
        except FileNotFoundError:
            print("Hata! Dosya açılamadı veya henüz bir kayıt yok.")
            break

        print("-"*30)
        print(f"Toplam {len(eslesen_kitaplar)} adet kitap bulundu.")
        print("-"*30)

        for i in range(len(eslesen_kitaplar)):
            print("|".join(eslesen_kitaplar[i]))
        while True:
            secim2 = input("Yeniden bir arama için 0'ı, Anamenüye dönmek için 1'i tuşlayınız.") #ya da int(input())
            if secim2 == "0":
                break
            elif secim2 == "1":
                return
            else:
                print("Lütfen sadece 0 veya 1 tuşuna basınız.")
                continue
ana_menu()