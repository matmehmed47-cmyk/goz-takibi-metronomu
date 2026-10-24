# Göz Takibi Metronomu

Tek dosyalık (tarayıcıda çalışan) bir hızlı okuma ve göz egzersizi uygulaması. Kişisel kullanım için yapıldı: bir öğretmen ve yeğeni.

**Uygulamayı aç:** GitHub Pages bağlantısı (depo sayfasının sağ üstünde, "About" bölümünde).

## İçerik
- Göz Takibi Metronomu ve Öbek okuma
- Okuma egzersizleri: Kayan Metin, Buğulu Okuma, Mavi Perde, Tekrarlı Okuma
- Görme ve dikkat egzersizleri: Kelime Yakala, Yakaladın mı?, Sayıyı Yakala, Gözün Köprüsü, Sayı Avı, Hata Var mı?, Sırasıyla, Topları Takip Et, Değişeni Bul, N-Geri
- Günlük rutin (A/B günleri), Hatırlama Soruları (aralıklı tekrar), aylık okuma ölçümü
- Gruplar: yetişkin ve çocuk 1-2, 3-4, 5-6, 7-8. sınıf

İlerleme tarayıcının kendi hafızasında (localStorage) tutulur; başka cihaza taşınmaz.

## Dürüst not
Egzersizlerde kişinin o egzersizdeki başarısı artar. Bunun genel zekâya ya da okuma anlamaya geçtiğine dair kanıt zayıftır (Simons ve ark., 2016). Uygulama "beyin gelişimi" iddiasında bulunmaz. Kanıtı görece iyi olan kısımlar: Tekrarlı Okuma, kendini yoklama ve aralıklı tekrar.

## Yapı
- `index.html`: yayınlanan, derlenmiş uygulama
- `kaynak/sablon.html`: uygulamanın şablonu (kod)
- `kaynak/build.py`: şablona metin, kelime ve soruları yerleştirir
- `veri/`: metinler, sınıf atamaları, sorular, kelime listeleri (JSON)

Yeniden derlemek için (Python 3):

```
python3 kaynak/build.py kaynak veri
```

Çıktı `kaynak/metronom.html` olarak yazılır; yayın için `index.html` yerine kopyalanır.

## Kaynaklar ve telif
Metinlerin bir kısmı MEB ders kitaplarından, halk edebiyatından, Vikipedi ve Vikikaynak gibi açık kaynaklardan alınmış ya da bu proje için yazılmıştır. Her metnin kaynağı veri dosyalarında `kaynak` alanında yer alır. Ders kitabı parçalarının ve diğer metinlerin hakları ilgili sahiplerine aittir; bu depo ticari amaçla kullanılmamalıdır. Bir hak sahibi kaldırılmasını isterse ilgili metin çıkarılır.

Soruların ve çoğu çocuk metninin bir kısmı yapay zekâ yardımıyla yazılmış ve yine yapay zekâ yardımıyla denetlenmiştir; hatalı soru ya da bilgi olabilir.
