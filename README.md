# Göz Takibi Metronomu

Tek dosyalık (tarayıcıda çalışan) bir hızlı okuma ve göz egzersizi uygulaması. Kişisel kullanım için yapıldı: bir öğretmen ve yeğeni.

**Uygulamayı aç:** https://matmehmed47-cmyk.github.io/goz-takibi-metronomu/

## Uygulama gibi yükle (ana ekrana ekle)
- **Android (Chrome):** sayfayı aç, sağ üstteki üç nokta menüsünden "Uygulamayı yükle" ya da "Ana ekrana ekle".
- **iPhone / iPad (Safari):** Paylaş düğmesi, sonra "Ana Ekrana Ekle".
- **Bilgisayar (Chrome / Edge):** adres çubuğunun sağındaki yükleme simgesi.

Yüklendikten sonra tam ekran açılır, internet olmadan da çalışır (ilk açılıştan sonra). İnternet varken her açılışta en yeni sürümü alır. Egzersiz çalışırken ekranın kararmasını engellemeye çalışır (tarayıcı destekliyorsa).

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
- `manifest.webmanifest`, `sw.js`, `simge/`: uygulama gibi yükleme, çevrimdışı çalışma ve simgeler
- `kaynak/sablon.html`: uygulamanın şablonu (kod)
- `kaynak/build.py`: şablona metin, kelime ve soruları yerleştirir
- `veri/`: metinler, sınıf atamaları, sorular, kelime listeleri (JSON)

Yeniden derlemek için (Python 3):

```
python3 kaynak/build.py kaynak veri
```

Çıktı `kaynak/metronom.html` olarak yazılır. Sonra yüklenebilir sürümü üretmek için:

```
python3 kaynak/pwa_yap.py
```

Bu, `index.html`, `manifest.webmanifest` ve `sw.js` dosyalarını yeniden yazar (`SURUM=70 python3 kaynak/pwa_yap.py` ile önbellek adı güncellenir). Simgeleri yeniden üretmek için `python3 kaynak/ikon_yap.py` (PIL gerekir).

## Kaynaklar ve telif
Metinlerin bir kısmı MEB ders kitaplarından, halk edebiyatından, Vikipedi ve Vikikaynak gibi açık kaynaklardan alınmış ya da bu proje için yazılmıştır. Her metnin kaynağı veri dosyalarında `kaynak` alanında yer alır. Ders kitabı parçalarının ve diğer metinlerin hakları ilgili sahiplerine aittir; bu depo ticari amaçla kullanılmamalıdır. Bir hak sahibi kaldırılmasını isterse ilgili metin çıkarılır.

Soruların ve çoğu çocuk metninin bir kısmı yapay zekâ yardımıyla yazılmış ve yine yapay zekâ yardımıyla denetlenmiştir; hatalı soru ya da bilgi olabilir.
