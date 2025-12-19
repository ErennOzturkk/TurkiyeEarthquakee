# TÜRKİYE İL BAZLI DEPREM RİSK ANALİZİ PROJESİ

---

## KAPAK SAYFASI

**Öğrenci Adı:** [Adınızı Buraya Yazın]  
**Öğrenci Soyadı:** [Soyadınızı Buraya Yazın]  
**Öğrenci Numarası:** [Numaranızı Buraya Yazın]  
**Ders Adı:** [Ders Adını Buraya Yazın]  
**Proje Konusu:** Türkiye İl Bazlı Deprem Risk Analizi ve İnteraktif Harita Uygulaması  
**Tarih:** [Tarihi Buraya Yazın]

---

## PROJE KONUSU

**Konu:** Türkiye İl Bazlı Deprem Risk Analizi

Bu proje, Türkiye'nin 81 ilini kapsayan kapsamlı bir deprem risk analizi gerçekleştirmektedir. Proje, fay hatları, tarihsel deprem verileri, bina stoğu ve nüfus verilerini kullanarak her il için bir risk skoru hesaplamaktadır. Analiz sonuçları, interaktif bir web uygulaması (Streamlit) ile görselleştirilmiştir.

---

## ÇALIŞMA KAYNAKLARI

Proje geliştirme sürecinde aşağıdaki kaynaklardan yararlanılmıştır:

1. **Python Kütüphaneleri ve Dokümantasyonları:**
   - GeoPandas: Mekansal veri analizi için
   - Pandas: Veri işleme ve analiz için
   - Streamlit: Web uygulaması geliştirme için
   - Folium: İnteraktif harita oluşturma için
   - Matplotlib: Görselleştirme için

2. **Veri Kaynakları:**
   - Türkiye İl Sınırları (GeoJSON formatı)
   - Türkiye Fay Hatları (Shapefile formatı)
   - Tarihsel Deprem Verileri (Excel formatı)
   - Bina Stoğu Verileri (Excel formatı)
   - Nüfus Verileri (CSV formatı)

3. **Öğrenme Kaynakları:**
   - Python GeoPandas dokümantasyonu
   - Streamlit dokümantasyonu ve örnekleri
   - GitHub'da benzer projeler
   - ChatGPT ile kod geliştirme ve hata ayıklama

4. **Referans Materyaller:**
   - Deprem risk analizi metodolojileri
   - Mekansal veri analizi teknikleri
   - Web uygulaması geliştirme best practices

---

## HAFTALIK ÇALIŞMA ÖZETLERİ

---

### 1. HAFTA: PROJE BELİRLENMESİ VE VERİ TOPLANMASI

**Tarih:** [1. Hafta Tarihi]

**Çalışma Özeti:**

Bu hafta, proje konusunun belirlenmesi ve gerekli verilerin toplanması ile geçmiştir.

**Yapılan İşlemler:**

1. **Proje Konusu Belirleme:**
   - Türkiye'nin deprem riski açısından kritik bir konumda olması nedeniyle, il bazlı deprem risk analizi projesi seçilmiştir.
   - Proje kapsamı: 81 il için risk skoru hesaplama ve görselleştirme

2. **Veri Kaynakları Araştırma:**
   - Türkiye il sınırları verisi (GeoJSON formatı) bulundu
   - Türkiye fay hatları verisi (Shapefile formatı) temin edildi
   - Tarihsel deprem verileri (M4.0+ büyüklüğünde) toplandı
   - Bina stoğu verileri (1980 öncesi ve 1981-2000 arası bina oranları) bulundu
   - İl bazlı nüfus verileri temin edildi

3. **Veri İnceleme ve Hazırlık:**
   - Veri formatları kontrol edildi
   - Eksik veya hatalı veriler tespit edildi
   - Veri yapıları analiz edildi
   - Veri birleştirme stratejisi belirlendi

4. **Teknoloji Stack Belirleme:**
   - Python programlama dili seçildi
   - GeoPandas, Pandas, Streamlit kütüphaneleri belirlendi
   - Geliştirme ortamı kuruldu (Jupyter Notebook)

**Sonuç:**
- Tüm gerekli veriler toplandı ve proje için uygun formata getirildi
- Proje yapısı ve metodoloji belirlendi
- Bir sonraki hafta için model geliştirme aşamasına geçiş hazırlığı tamamlandı

---

### 2. HAFTA: MODEL V1 VE V2 ÇALIŞMALARI

**Tarih:** [2. Hafta Tarihi]

**Çalışma Özeti:**

Bu hafta, deprem risk analizi için model geliştirme çalışmaları yapılmıştır. İlk olarak temel bir model (V1) oluşturulmuş, ardından iyileştirmeler yapılarak Model V2 geliştirilmiştir.

**Yapılan İşlemler:**

1. **Model V1 Geliştirme:**
   - Temel risk skoru hesaplama formülü oluşturuldu
   - Fay hatlarına yakınlık analizi yapıldı (10km buffer)
   - İl bazlı fay tehlike oranı hesaplandı
   - Basit bir risk skoru formülü uygulandı

2. **Model V2 Geliştirme:**
   - Tarihsel deprem verileri entegre edildi
   - İl sınırları içindeki M4.0+ deprem sayısı hesaplandı
   - Risk skoru formülü geliştirildi:
     - Toplam Tehlike = %70 Fay Tehlike + %30 Tarihsel Tehlike
     - Risk Skoru = %50 Toplam Tehlike + %50 Kırılganlık (Eski Bina Oranı)
   - Kırılganlık faktörü (2000 öncesi bina oranı) eklendi
   - Nüfus verileri entegre edildi

3. **Veri İşleme:**
   - İl adı normalleştirme fonksiyonu geliştirildi (Türkçe karakter sorunları için)
   - Mekansal veri birleştirme işlemleri yapıldı
   - Koordinat sistemi dönüşümleri gerçekleştirildi (WGS84 → EPSG:32637)
   - Min-Max normalizasyon uygulandı (0-1 arası puanlar)

4. **Görselleştirme:**
   - Model V2 sonuçları için risk haritası oluşturuldu
   - En riskli 10 il listesi çıkarıldı
   - GeoJSON formatında çıktı dosyası oluşturuldu

**Sonuç:**
- Model V2 başarıyla geliştirildi ve test edildi
- Risk skorları 1-10 arası ölçekte hesaplanıyor
- Model V2 sonuçları kaydedildi (GeoJSON ve PNG formatında)
- Model V3 için iyileştirme alanları belirlendi

---

### 3. HAFTA: MODEL V3 VE STREAMLIT ENTEGRASYONU

**Tarih:** [3. Hafta Tarihi]

**Çalışma Özeti:**

Bu hafta, Model V3 geliştirilmiş ve Streamlit ile interaktif web uygulaması oluşturulmuştur.

**Yapılan İşlemler:**

1. **Model V3 Geliştirme:**
   - Tarihsel deprem analizi iyileştirildi:
     - İl sınırlarına 50km etki alanı (buffer) eklendi
     - Deprem sayısı yerine büyüklük toplamı kullanıldı
     - Ege Denizi ve komşu ülkelerdeki depremlerin etkisi dahil edildi
   - Risk skoru formülü korundu:
     - Toplam Tehlike = %70 Fay + %30 Tarihsel (Büyüklük Toplamı)
     - Risk Skoru = %50 Toplam Tehlike + %50 Kırılganlık
   - Model V3 sonuçları oluşturuldu ve kaydedildi

2. **Streamlit Uygulaması Geliştirme:**
   - Streamlit framework'ü öğrenildi
   - Ana uygulama dosyası (`streamlit_harita.py`) oluşturuldu
   - Folium ile interaktif harita entegrasyonu yapıldı
   - Özellikler:
     - İnteraktif harita (tıklama ile il seçimi)
     - Dropdown menü ile il seçimi
     - İl bazlı detaylı risk bilgileri gösterimi
     - En riskli 10 il tablosu
     - Renk kodlu risk gösterimi (Yeşil: Düşük, Turuncu: Orta, Kırmızı: Yüksek, Koyu Kırmızı: Çok Yüksek)
   - Sidebar bilgi paneli eklendi
   - Responsive tasarım uygulandı

3. **Veri Entegrasyonu:**
   - Model V3 GeoJSON dosyası Streamlit uygulamasına entegre edildi
   - Veri yükleme optimizasyonu yapıldı (`@st.cache_data` kullanıldı)
   - Hata yönetimi eklendi

4. **Test ve İyileştirme:**
   - Uygulama test edildi
   - Kullanıcı deneyimi iyileştirildi
   - README dosyası oluşturuldu (`README_STREAMLIT.md`)
   - Requirements.txt dosyası hazırlandı

**Sonuç:**
- Model V3 başarıyla geliştirildi ve Streamlit uygulamasına entegre edildi
- İnteraktif web uygulaması çalışır durumda
- Kullanıcılar haritada illere tıklayarak detaylı risk bilgilerini görebiliyor
- Proje teslim için hazır hale getirildi

---

### 4. HAFTA: PROJE TESLİMİ

**Tarih:** [4. Hafta Tarihi]

**Çalışma Özeti:**

Bu hafta, proje son kontrolleri yapılmış, dokümantasyon tamamlanmış ve proje teslim edilmiştir.

**Yapılan İşlemler:**

1. **Proje Son Kontrolleri:**
   - Tüm kodlar gözden geçirildi
   - Hata ayıklama yapıldı
   - Kod yorumları eklendi
   - Dosya yapısı düzenlendi

2. **Dokümantasyon:**
   - Proje dokümanı hazırlandı (bu doküman)
   - README dosyası güncellendi
   - Kod içi dokümantasyon tamamlandı
   - Kullanım kılavuzu oluşturuldu

3. **Görselleştirme ve Sunum:**
   - Risk haritaları (V2 ve V3) oluşturuldu
   - En riskli iller listesi hazırlandı
   - Proje özeti hazırlandı

4. **Proje Dosyaları:**
   - Tüm kaynak kodlar düzenlendi
   - Veri dosyaları organize edildi
   - Çıktı dosyaları (GeoJSON, PNG) kaydedildi
   - Requirements.txt dosyası hazırlandı

5. **YouTube Video Hazırlığı:**
   - Proje tanıtım videosu için içerik planlandı
   - Video linki: [YouTube video linkinizi buraya ekleyin]

**Sonuç:**
- Proje başarıyla tamamlandı
- Tüm dokümantasyon hazırlandı
- Proje teslim edildi

---

## PROJE ÖZETİ

### Proje Amacı
Türkiye'nin 81 ili için deprem risk analizi yaparak, her il için bir risk skoru hesaplamak ve bu sonuçları interaktif bir web uygulaması ile görselleştirmek.

### Kullanılan Teknolojiler
- **Python 3.8+**
- **GeoPandas**: Mekansal veri analizi
- **Pandas**: Veri işleme
- **Streamlit**: Web uygulaması
- **Folium**: İnteraktif harita
- **Matplotlib**: Görselleştirme

### Model Metodolojisi

**Model V3 (Final Model):**
- **Fay Tehlike Puanı**: İl alanının fay hatlarına 10km yakınlık oranı
- **Tarihsel Tehlike Puanı**: İl sınırlarının 50km etki alanındaki M4.0+ depremlerin büyüklük toplamı
- **Toplam Tehlike**: %70 Fay + %30 Tarihsel
- **Kırılganlık Puanı**: 2000 öncesi bina oranı
- **Risk Skoru**: %50 Toplam Tehlike + %50 Kırılganlık (1-10 arası ölçek)

### Proje Çıktıları
1. Model V1, V2, V3 sonuçları (GeoJSON formatında)
2. Risk haritaları (PNG formatında)
3. En riskli 10 il listesi
4. İnteraktif Streamlit web uygulaması
5. Proje dokümantasyonu

---

## YOUTUBE VİDEO LİNKİ

**Proje Tanıtım Videosu:** [YouTube video linkinizi buraya ekleyin]

Video içeriği:
- Proje tanıtımı
- Model metodolojisi açıklaması
- Streamlit uygulaması demo
- Sonuçların değerlendirilmesi

---

## SONUÇ

Bu proje kapsamında, Türkiye'nin 81 ili için kapsamlı bir deprem risk analizi gerçekleştirilmiştir. Model V3 ile geliştirilen risk skoru hesaplama sistemi, fay hatları, tarihsel deprem verileri ve bina stoğu verilerini birleştirerek her il için 1-10 arası bir risk skoru üretmektedir. Streamlit ile geliştirilen interaktif web uygulaması sayesinde, kullanıcılar haritada illere tıklayarak detaylı risk bilgilerini görüntüleyebilmektedir.

Proje, 4 haftalık bir süreçte tamamlanmış ve başarıyla teslim edilmiştir.

---

**Proje Tarihi:** [Başlangıç Tarihi] - [Bitiş Tarihi]  
**Toplam Süre:** 4 Hafta  
**Durum:** ✅ Tamamlandı

