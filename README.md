# 📚 Python Console-Based Library Management System

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> **💡 Geliştirici Notu:**
> Bu mini-projeyi, üniversitedeki *Python - Nesneye Dayalı Modelleme* dersinde öğrendiğim temel algoritmaları pekiştirmek ve Coursera'dan tamamladığım **"IBM Python for Data Science, AI & Development"** kursundaki veri işleme yetkinliklerimi somut bir konsol uygulamasına dökmek amacıyla geliştirdim.

Bu proje, Python temel programlama mantığı, döngüler ve string metotları kullanılarak geliştirilmiş konsol tabanlı bir Kütüphane Yönetim Sistemidir. Harici bir kütüphane veya veritabanı kullanılmadan, dosya işlemleri (File I/O) ile verilerin kalıcı olarak `.txt` formatında saklanması ve işlenmesi amaçlanmıştır.

## 🚀 Proje Amacı ve Vizyonu

Bu sistemin temel odak noktası sadece veri eklemek değil, **Veri Bütünlüğünü (Data Integrity)** ve **İş Kurallarını (Business Logic)** sağlamaktır. Kullanıcıdan alınan ham veriler, sisteme kaydedilmeden önce çeşitli doğrulama (validation) aşamalarından geçirilerek veri tabanının (text dosyasının) sağlığı korunmuştur.

## ✨ Temel Özellikler

* **📖 Dinamik Veri Girişi:** Sistem, arka arkaya 25 adet kitabın girilmesine olanak tanıyan kesintisiz bir döngüye sahiptir.
* **🛡️ Gelişmiş Doğrulama (Validation):**
  * **Kitap ve Yazar Adı:** Boş geçilmesi `len()` kontrolleri ile engellenmiştir. Noktalama işaretlerine esneklik tanınarak gerçek dünya verilerine uyum sağlanmıştır.
  * **ISBN Kontrolü:** Girilen değerin sadece rakamlardan oluşması (`isdigit()`) ve tam 10 haneli olması zorunlu kılınmıştır.
  * **Yayın Yeri:** Şehir isimlerinde rakam kullanılmaması için string analiz metotları (`isalpha()`) ile güvenlik katmanı oluşturulmuştur.
* **🔍 Akıllı Arama ve Filtreleme Motoru:** * Kitap adında geçen parçalı kelimeye göre esnek arama (`in` operatörü).
  * ISBN numarasının başlangıç değerine göre arama (`startswith()`).
  * Yazar soyadına göre tam eşleşmeli arama (Metin bölme işlemleri ile).
* **💾 Kalıcı Veri Depolama:** Tüm kayıtlar `kitaplar.txt` dosyasına, ayrıştırmayı kolaylaştırmak için `|` separatörü kullanılarak kaydedilir.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python (Built-in functions)
* **Veri Yapıları:** Listeler, Döngüler (While/For), Karar Yapıları (If/Elif/Else)
* **Depolama:** File I/O (`open()`, `read()`, `write()`, `append()`)

## 💻 Kurulum ve Kullanım

Sistemi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Projeyi bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/TunahanMazi/Basic-Library-Management-System.git](https://github.com/TunahanMazi/Basic-Library-Management-System.git)
